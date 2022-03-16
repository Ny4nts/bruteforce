# coding=utf-8
import base64

f1 = open('base_encode.txt', 'r')
str1 = f1.readlines()
for i in str1:
        ds = base64.b64decode(i.encode("utf-8")).decode("utf-8")
        print(ds)
