"""
Author:Nguyễn Mạnh Trung
Date: 11/10/2021
Problem:Assume that the variable data refers to the dictionary {'b':20, 'a':35}. Write the
    expressions that perform the following tasks:
    a. Replace the value at the key 'b' in data with that value’s negation.
    b. Add the key/value pair 'c':40 to data.
    c. Remove the value at key 'b' in data, safely.
    d. Print the keys in data in alphabetical order.
Solution:
    ....
"""
data = {'b': 20, 'a': 35}

x = data.get("b")
data["b"]=-x
print(data)

data.update({"c":40})
print(data)

data.pop("b")
print(data)

dict_keys = data.keys()
keyList = []
for key in dict_keys:
    keyList.append(key)
keyList.sort()
print(keyList)