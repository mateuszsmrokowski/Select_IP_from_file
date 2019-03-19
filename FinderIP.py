import re
from operator import itemgetter, attrgetter

file = open("hi.txt")

base = []
base.append([" ", 0])
my_bin = []
i = 1

def find_ip():
    for lines in file:
        global i
        ip = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",lines )
        temp = False
            
        if len(ip) >= 1:
            temp = False
            for x in range (len(ip)):
                temp = False
                for n in range(len(base)):
                    if ip[x] == base [n][0]:
                        base[n][1] += 1
                        temp = True
                if temp == False:
                    base.append([ip[x], 1])


def print_result():

    print '\n\nRESULT'
    for i in base:
       print i


base.pop(0)
find_ip()
print_result()

sorted(base, key=itemgetter(1), reverse = True)
