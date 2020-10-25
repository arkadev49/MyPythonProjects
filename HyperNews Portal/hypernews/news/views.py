from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from django.http import HttpResponse, Http404
from json import load, dump
from hypernews.settings import NEWS_JSON_PATH
from datetime import datetime
from random import randint


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return redirect('/news/')


class NewsView(View):
    def get(self, request, *args, **kwargs):
        search = request.GET.get('q')
        with open(NEWS_JSON_PATH, 'r') as json_file:
            read_json = load(json_file)
        read_json = sorted(read_json, key=lambda i: i['created'], reverse=True)
        news = []
        if search:
            for item in read_json:
                if search in item['title']:
                    news.append(item)
        else:
            news = read_json.copy()
        html_content = '<h2>Hyper news</h2>\n'
        html_content += '''<form action="/news/" method="get">
<p> Search : <input type="text" name="q" value="{}">
<button type="submit"> GO </button> </p>
</form>'''.format("" if search is None else search)
        prev_date = ''
        for nw in news:
            if nw['created'].split()[0] == prev_date:
                html_content += '<li><a target="_blank" href="/news/{}/">{}</a></li>\n'.format(str(nw['link']),
                                                                                               nw['title'])
            else:
                if prev_date != '':
                    html_content += '</ul>\n'
                html_content += '<h4>{}</h4>'.format(nw['created'].split()[0])
                prev_date = nw['created'].split()[0]
                html_content += '<ul>\n'
                html_content += '<li><a target="_blank" href="/news/{}/">{}</a></li>\n'.format(str(nw['link']),
                                                                                               nw['title'])

        html_content += '</ul>\n</li>\n'
        html_content += '<a target="_blank" href="/news/create/"> Create a Page </a>'
        return HttpResponse(html_content)


class ArticleView(View):
    def get(self, request, link, *args, **kwargs):
        with open(NEWS_JSON_PATH, 'r') as json_file:
            news = load(json_file)
        for nw in news:
            if int(link) == nw['link']:
                content = nw
                break
        else:
            raise Http404
        html_content = '''
        <h2>{}</h2>
        <p>{}</p>
        <p>{}</p>
        <a target="_blank" href="/news/"> Back to Main Page </a>'''.format(content['title'], content['created'],
                                                                           content['text'])
        return HttpResponse(html_content)


class CreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='form.html')

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        text = request.POST.get('text')
        with open(NEWS_JSON_PATH, 'r') as json_file:
            news = load(json_file)
        new_news = {
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "text": text,
            "title": title,
            "link": randint(1000000, 9999999)
        }
        news.append(new_news)
        with open(NEWS_JSON_PATH, 'w') as json_file:
            dump(news, json_file, indent=4)
        return redirect('/news/')


class SearchView(View):
    def get(self, request, *args, **kwargs):
        search = request.GET.get('q')
        return HttpResponse(search)
