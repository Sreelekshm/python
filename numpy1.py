import numpy as np
# # print(np.__version__)

# # number = np.array([10,20,30,40,50])
# # print(number)
# # print(type(number))



# # zeros() creates an arrays using __builtins__ function
# # a=np.zeros(5)
# # print("zeros :",a)


# # b= np.ones(5)    #to creating array of ones
# # print("ones:",b)


# # c= np .arange(1,11)     #generating value using  a start ,stop,and optional step.
# # print("range:",c)


# # d= np. arange(2,21,1) 
# # print("range with step:",d)



# # e= np. arange(1,21,2) 
# # print("range with step:",e)




# # e= np. linspace(1,10,3)       #linspace( generates a specified number of evenly spaced value)
# # print("linspace:",e)




# # a= np.array([10,20,30,40])     #one dimentional and two dimentional arrays
# # b= np.array([ [10,20,30], [40,50,60]])
# # print("1d array:")
# # print(a)


# # print("2d arry:")
# # print(b)


# # print("dimensions:",a.ndim)
# # print("shape:",a .shape)
# # print("total elements :",a.size)

# # print("dimensions:",b.ndim)
# # print("shape:",b.shape)
# # print("total elements :",b.size)



# # a =np.array([10,2,30])
# # b= np.array([1.5,2.5,3.5])
# # c=np.array([True,False,True])
# # z=np.zeros(5)
# # print(a.dtype)
# # print(b.dtype)
# # print(c.dtype)



# # marks = np.array([75,82,68,91,88])          #acces array elements using indexing
# # print("first mark:",marks[0])
# # print("thrid mark:",marks[2])
# # print("last mark:",marks[-1])


# # marks[1] =95

# # print("updated marks:",marks)



# # marks=np.array([65,70,80,85,90,95])

# # print("total:",np.sum(marks))
# # print("avaerage:",np.mean(marks))



# # marks=np.array([65,70,80,85,90,95])
# # print("total:",np.sum(marks))
# # print("mean:" ,np.mean(marks))
# # print("median:" ,np.median(marks))
# # print("minimum:", np.min(marks))
# # print("maximum:",np.max(marks))



# marks = np .array([[80,70,90],
#                   [60,85,75],
#                   [90,95,85]])
# print("student avarages:")
# print(np.mean(marks,axis=1))

# print("subject averages:")
# print(np.mean(marks,axis=0))

# print("student total:")
# print(np.sum(marks,axis=1))


# np.random.speed(10)
# a.np.random.randint(1,101,size=10)
# b.np.random.rand(5)


# print("random intergers:",a)
# print("random decimal:"b)


# marks= np.array([78,45,92,65,88,54])

# sorted_marks = np.sort(marks)
# print("ascending:",sorted_marks)

# print("descending:",np.sort(marks)[::-1])
# print("original:",marks)



# a=np.array([10,20,30])
# b=np.array([1,2,3])


# print("addition:",a+b)
# print("subtraction",a-b)
# print("muiltiplication",a*b)
# print("division",a/b)
# print("power",a**2)


# numbers =np.arange(1,13)


# matrix= numbers.reshape(3,4)
# print(numbers)
# print(matrix)
# print("shape:",matrix.shape)





# a= np.array([10,20,30])
# b= np.array([40,50,60])

# print("concatenate:",np.concatenate((a,b)))
# print("vertical stack:", np.vstack((a,b)))
# print("horizontal stack:",np.hstack((a,b)))


marks= np.array ([45,78,32,90,65,28,85])
passed = marks[marks>=40]
failed= marks[marks<=40]
high_score =marks=marks[marks>=80]
print("passed:",passed)
print("failed:",failed)
print("high score:",high_score)
