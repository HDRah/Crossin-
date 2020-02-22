"""
Created on Fri Dec 19 10:27:28 2019

@author: Zhou Yihong
"""
import hashlib
import base64
test = []
target = 'NDRiMWZmMmVjZTk5MTFjMWI1MDNkYTY0MzZlYTAzMTA=\n'.encode('utf-8')

mm = hashlib.md5()
mm.update("我们在一起吧".encode('utf-8'))
m = base64.encodestring(mm.hexdigest().encode('utf-8'))
test.append(m)

mm = hashlib.md5()
mm.update("我选择原谅你".encode('utf-8'))
m = base64.encodestring(mm.hexdigest().encode('utf-8'))
test.append(m)

mm = hashlib.md5()
mm.update("别说话，吻我".encode('utf-8'))
m = base64.encodestring(mm.hexdigest().encode('utf-8'))
test.append(m)

mm = hashlib.md5()
mm.update("多喝热水".encode('utf-8'))
m = base64.encodestring(mm.hexdigest().encode('utf-8'))
test.append(m)
a = test.index(target)
print(a+1)