# coding=utf-8
import base64


f1 = open('pass200.txt', 'r')
str1 = f1.readlines()
for i in str1:
        es = base64.b64encode(i.encode("utf-8")).decode("utf-8")
        print(es)
