from django.views import View
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, redirect


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'menu.html')


class TicketView(View):
    line_of_cars = {'change_oil': [],
                    'inflate_tires': [],
                    'diagnostic': []}

    def get(self, request, ticket_name, *args, **kwargs):
        est = 0
        if ticket_name in ['change_oil', 'inflate_tires', 'diagnostic']:
            ticket_number = 0
            for items in self.line_of_cars:
                if self.line_of_cars[items]:
                    for nums in self.line_of_cars[items]:
                        if nums > ticket_number:
                            ticket_number = nums
            ticket_number += 1
            if ticket_name == 'change_oil':
                est = len(self.line_of_cars['change_oil']) * 2
                self.line_of_cars['change_oil'].append(ticket_number)
            elif ticket_name == 'inflate_tires':
                est = len(self.line_of_cars['change_oil']) * 2 \
                      + len(self.line_of_cars['inflate_tires']) * 5
                self.line_of_cars['inflate_tires'].append(ticket_number)
            else:
                est = len(self.line_of_cars['change_oil']) * 2 \
                      + len(self.line_of_cars['inflate_tires']) * 5 \
                      + len(self.line_of_cars['diagnostic']) * 30
                self.line_of_cars['diagnostic'].append(ticket_number)
            html_content = '''<div>Your number is {}</div>
<div>Please wait around {} minutes</div>'''.format(ticket_number, est)
            return HttpResponse(html_content)
        else:
            raise Http404


class ProcessingView(View):
    processed_ticket = []

    def get(self, request, *args, **kwargs):
        context = {
            'change_oil': len(TicketView.line_of_cars['change_oil']),
            'inflate_tires': len(TicketView.line_of_cars['inflate_tires']),
            'diagnostic': len(TicketView.line_of_cars['diagnostic']),
        }
        return render(request, 'process.html', context=context)

    def post(self, request, *args, **kwargs):
        if self.processed_ticket:
            self.processed_ticket.pop()
        if TicketView.line_of_cars['change_oil']:
            self.processed_ticket.append(TicketView.line_of_cars['change_oil'].pop(0))
        elif TicketView.line_of_cars['inflate_tires']:
            self.processed_ticket.append(TicketView.line_of_cars['inflate_tires'].pop(0))
        elif TicketView.line_of_cars['diagnostic']:
            self.processed_ticket.append(TicketView.line_of_cars['diagnostic'].pop(0))
        return redirect('/next')


class NextView(View):
    def get(self, request, *args, **kwargs):
        if ProcessingView.processed_ticket:
            return HttpResponse('<div>Next ticket #{}</div>'.format(ProcessingView.processed_ticket[0]))
        return HttpResponse('<div>Waiting for the next client</div>')
