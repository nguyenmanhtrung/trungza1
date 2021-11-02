"""
Author:Nguyễn Mạnh Trung
Date: 11/10/2021

Problem:
            A group of statisticians at a local college has asked you to create a set of functions
that compute the median and mode of a set of numbers, as defined in Section
5.4. Define these functions in a module named stats.py. Also include a function
named mean, which computes the average of a set of numbers. Each function
should expect a list of numbers as an argument and return a single number. Each
function should return 0 if the list is empty. Include a main function that tests the
three statistical functions with a given list
Solution:
    ....
"""
import statistics

print("//////Enter set of numbers//////")
print("/////To stop entering number enter */////")
var = True
number_list = []

while (var == True):
    num = input("Enter number : ")
    if (num == '*'):
        var = False
        break
    else:
        num = int(num)
        number_list.append(num)
print("/////your input LIST is :")
print(number_list)
print()



def median(number_list):
    length = len(number_list)
    if ((length % 2) == 0):
        first = number_list[int((length / 2)) - 1]
        second = number_list[int(length / 2)]
        i = (first + second) / 2
        return i
    else:
        return number_list[length // 2]



def mode(number_list):
    return statistics.mode(number_list)



def mean(number_list):
    return statistics.mean(number_list)


print("Median of the given list is:", median(number_list))
print()
print("Median of the given list is:", mean(number_list))
print()
print("Median of the given list is:", mode(number_list))


