# 1
# for i in range(2000,3200):
#     if i%7==0 and i%5==0:
#         pass
#     elif i%7==0:
#         print(i,end=", ")

# 2
# fact = 1
# num = int(input("Enter the number: "))

# if(num < 0 or num==0):
#     print("Sorry")
# else:
#     for i in range(1,num+1):
#         fact = fact*i

# print(fact)

# 3
# dic = {}

# num = int(input("Enter the number: "))

# for i in range(1,num+1):
#     dic[i] = i*i
# print(dic)

# 4

# li = input("Enter").split(",")
# tup = tuple(li)
# print(li)
# print(tup)

# 5

# class teststring:
#     def __init__(self,x):
#         self.x = x

#     def takestring(self):
#         print(self.x)

#     def printString(self):
#         print(self.x.upper())

# def test():
#     s = teststring("test string")
#     s.takestring()
#     s.printString()

# test()

# 6

# import math
# C = 50
# H = 30
# D = input().split(",")

# for i in D:
#     formula = round(math.sqrt((2*C*int(i))/H))
#     print(formula,end=" ")


# 7
# num = input("Enter x and y: ").split(',')

# li = []

# for i in range(0,int(num[0])):
#     temp = []
#     for j in range(0,int(num[1])):
#         temp.append(i*j)
#     li.append(temp)

# print(li)


# 8

# strings = input().split(',')
# strings.sort()
# print(strings)


# 9
# li = []
# while(True):
#     x = input("Enter the sentence: ")
#     if x:
#         li.append(x)
#     else:
#         break

# for i in li:
#     print(i.upper())

# 10
# Li = [5,10,20,4,8,7,9,20,30]

# li = []

# while(len(Li)>0):
#     mininum = min(Li)
#     li.append(mininum)
#     Li.remove(mininum)

# print(li)