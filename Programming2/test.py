# print("Hello world")


# n  = 'greetings'

# count  = 0

# # for i in n:
# #     print(n)
# #     count = count + 1

# # print(count)


# # string slicing
         
# sliced  = n[0:len(n):2]    # [starting point, endpoint(non inclusive),step]
# print(sliced)

# t  = 'anique'

# print(t[1:len(t):2])

# print(t[-1:len(n)])



# def func(y):

#   return b+y

# b = 5

# print(func(6))

# data = ['Jake', 'John']
# s = {i : [x for x in range(2)] for i in data}
# print(s)


 #LAMBDA Funtions
'''
1. Nameless
2. One liner
3. Pure functions
'''

# x = 5
# def name(x,y):
#     return x+y
    
# name()

 # lambda input variables:output expression

# x = lambda x,y : x * y if x % 2 == 0 and y % 2 == 0
# print(x(4,3))


'''
Write a program, which will find all such numbers between 
1000 and 3000 (both included) such that each digit of the 
number is an even number.
The numbers obtained should be printed in a comma-separated 
sequence on a single line.

'''

# for i in range(1000,3000):

#     i  = str(i)
#     if int(i[0]) % 2 == 0 and  int(i[1]) % 2== 0 and int(i[2]) % 2== 0 and int(i[3]) % 2== 0:
#         print(int(i) , " , " , end = " ")


'''
Write a program which takes 2 digits, X,Y as input and generates a 2- dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

'''
# x = 5
# y = 6
# outer = []
# for i in range(x):  # rows outer loop
#     inner = []
#     for j in range(y): #cols inner loop\
#         inner.append(i * j)
        
#     outer.append(inner)


# print(outer)



