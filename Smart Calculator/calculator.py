class Calculator:
    var_dict = {}
    operators = ['+', '-', '*', '/', '^']

    def is_variable(self, exp):
        for i in exp:
            if i in self.operators:
                return False
            elif '=' in i:
                return False
        return True

    def valid_parenthesis(self, exp):
        if exp.count('(') == 0 and exp.count(')') == 0:
            return True
        if exp.count('(') != exp.count(')'):
            return False
        stk = []
        for i in exp:
            if i == '(':
                stk.append('(')
            elif i == ')':
                try:
                    stk.pop()
                except IndexError:
                    return False
        if not self.isEmpty(stk):
            return False
        return True

    def validate_expression(self, exp):
        if not self.valid_parenthesis(exp):
            print('Invalid expression')
            return False
        if ' ' in exp:
            exp = exp.replace('(', '( ')
            exp = exp.replace(')', ' )')
            exp = exp.split()
        else:
            exp = [char for char in exp]
        for i in range(len(exp)):
            if exp[i].count('*') > 1 or exp[i].count('/') > 1:
                print('Invalid expression')
                return False
            if exp[i].count('+') > 1:
                exp[i] = '+'
            elif exp[i].count('-') > 1:
                if exp[i].count('-') % 2 == 0:
                    exp[i] = '+'
                else:
                    exp[i] = '-'
        new_exp = ''
        for char in exp:
            new_exp += char + ' '
        return new_exp

    @staticmethod
    def isEmpty(stk):
        return True if stk == [] else False

    @staticmethod
    def peek(stk):
        return stk[len(stk) - 1] if stk else '\0'

    @staticmethod
    def precedence(op):
        if op == '^':
            return 3
        elif op == '*' or op == '/':
            return 2
        elif op == '+' or op == '-':
            return 1
        return -1

    def infix_to_postfix(self, exp):
        if ' ' in exp:
            exp = exp.replace('(', '( ')
            exp = exp.replace(')', ' )')
            exp = exp.split()
        else:
            exp = [char for char in exp]
        stk = []
        res = ''
        for i in exp:
            if i.isalnum():
                res += i + ' '
            elif i in self.operators:
                if self.isEmpty(stk) or self.peek(stk) == '(':
                    stk.append(i)
                elif self.precedence(i) > self.precedence(self.peek(stk)):
                    stk.append(i)
                elif self.precedence(i) <= self.precedence(self.peek(stk)):
                    while stk:
                        res += stk.pop() + ' '
                        if self.peek(stk) == '(' or self.precedence(i) < self.precedence(self.peek(stk)):
                            break
                    stk.append(i)
            elif i == '(':
                stk.append(i)
            elif i == ')':
                while stk:
                    res += stk.pop() + ' '
                    if self.peek(stk) == '(':
                        stk.pop()
                        break
        while stk:
            res += stk.pop() + ' '
        return res

    def postfix_eval(self, exp):
        stk = []
        if ' ' in exp:
            exp = exp.replace('(', '( ')
            exp = exp.replace(')', ' )')
            exp = exp.split()
        else:
            exp = [char for char in exp]
        for i in exp:
            if i.isnumeric():
                stk.append(int(i))
            elif i in self.operators:
                if len(stk) > 1:
                    a = stk.pop()
                    b = stk.pop()
                    if i == '+':
                        stk.append(b + a)
                    elif i == '-':
                        stk.append(b - a)
                    elif i == '*':
                        stk.append(b * a)
                    elif i == '/':
                        stk.append(b // a)
                    elif i == '^':
                        stk.append(b ^ a)
            else:
                if i in self.var_dict:
                    stk.append(self.var_dict[i])
                else:
                    print('Unknown variable')
                    return
        return stk.pop()

    # def solve_expression(self, exp):
    #     s = 0
    #     prev = '+'
    #     for i in exp:
    #         if self.isnumeric(i):
    #             if prev == '+':
    #                 s = s + int(i)
    #             else:
    #                 s = s - int(i)
    #         elif i in self.var_dict:
    #             if prev == '+':
    #                 s = s + self.var_dict[i]
    #             elif prev == '-':
    #                 s = s - self.var_dict[i]
    #         else:
    #             if '+' in i:
    #                 prev = '+'
    #             else:
    #                 prev = '+' if i.count('-') % 2 == 0 else '-'
    #     print(s)

    # def is_valid_expression(self, exp):
    #     for i in range(1, len(exp), 2):
    #         if exp[i] not in self.operators:
    #             return False
    #     return True

    @staticmethod
    def execute_command(val):
        if val == 'exit':
            print('Bye!')
            exit(0)
        elif val == 'help':
            print('The program calculates the sum of numbers')
        else:
            print('Unknown command')

    @staticmethod
    def is_get_value(val):
        return True if ' ' not in val and '=' not in val else False

    def print_value(self, val):
        if self.isnumeric(val):
            print(val)
            return
        if not self.check_var_std(val):
            print('Invalid identifier')
            return
        if val not in self.var_dict:
            print('Unknown variable')
        else:
            print(self.var_dict[val])

    @staticmethod
    def isnumeric(val):
        try:
            __ = int(val)
            return True
        except ValueError:
            return False

    def check_var_std(self, var):
        num = False
        alpha = False
        for i in var:
            if self.isnumeric(i):
                num = True
            elif i.isalpha():
                alpha = True
            if num and alpha:
                return False
        if not num and not alpha:
            return False
        return True

    @staticmethod
    def is_assignment(exp):
        return True if '=' in exp else False

    def assign(self, exp):
        if exp.count('=') > 1:
            print('Invalid assignment')
            return
        exp = exp.replace(' ', '')
        var = exp[:exp.index('=')]
        val = exp[exp.index('=') + 1:]
        if self.check_var_std(var):
            if self.isnumeric(val):
                self.var_dict[var] = int(val)
            else:
                if self.check_var_std(val):
                    if val in self.var_dict:
                        self.var_dict[var] = self.var_dict[val]
                    else:
                        print('Unknown variable')
                else:
                    print('Invalid assignment')
        else:
            print('Invalid identifier')

    def execute(self, exp):
        if exp == '':
            return
        if exp.startswith('/'):
            self.execute_command(exp[1:])
        elif '=' in exp:
            self.assign(exp)
        elif self.isnumeric(exp):
            print(exp)
        elif self.is_variable(exp):
            self.print_value(exp)
        else:
            valid = self.validate_expression(exp)
            if valid:
                print(self.postfix_eval(self.infix_to_postfix(valid)))


cal = Calculator()
while True:
    inp = input()
    cal.execute(inp)
