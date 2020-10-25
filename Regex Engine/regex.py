import sys

sys.setrecursionlimit(10000)


def matchChar(regex, string):
    if regex == '' and string == '':
        return True
    if regex == '':
        return True
    if string == '':
        return False
    if regex == '.' and string != '':
        return True
    if regex == string:
        return True
    return False


def matchEquals(regex, string):
    if not regex:
        return True
    else:
        if not string:
            if regex.endswith('$') or regex.endswith('*'):
                return True
            else:
                return False
        else:
            if len(regex) > 1:
                if regex[1] in ['?', '*'] and not matchChar(regex[0], string[0]):
                    return matchEquals(regex[2:], string)
                if regex[1] in ['?'] and matchChar(regex[0], string[0]):
                    return matchEquals(regex[2:], string[1:])
                if regex[1] in ['*', '+'] and matchChar(regex[0], string[0]):
                    if regex[2:3] == string[1:2] or regex[2:3] == '':
                        return matchEquals(regex[2:], string[1:])
                    else:
                        return matchEquals(regex, string[1:])
            if matchChar(regex[0], string[0]):
                return matchEquals(regex[1:], string[1:])
            else:
                return False


def checkRegex(regex, string):
    if not string:
        if regex == '':
            return True
        else:
            return False
    if regex.startswith('^'):
        if matchEquals(regex[1:], string):
            return True
        else:
            return False
    if matchEquals(regex, string):
        return True
    return checkRegex(regex, string[1:])


reg, inp = input().split('|')
inp = inp.replace('\\', '\\\\').replace('^', '_').replace('$', '`')
reg = reg.replace('\\^', '_').replace('\\$', '`').replace('\\?', '~').replace('\\*', '[')
reg = reg.replace('\\+', ']').replace('\\.', ';')
inp = inp.replace('?', '~').replace('*', '[').replace('+', ']').replace('.', ';')
print(checkRegex(reg, inp))
