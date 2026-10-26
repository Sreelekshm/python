import numpy as np
# print(np.__version__)

# number = np.array([10,20,30,40,50])
# print(number)
# print(type(number))



# zeros() creates an arrays using __builtins__ function
# a=np.zeros(5)
# print("zeros :",a)


# b= np.ones(5)    #to creating array of ones
# print("ones:",b)


# c= np .arange(1,11)     #generating value using  a start ,stop,and optional step.
# print("range:",c)


# d= np. arange(2,21,1) 
# print("range with step:",d)



# e= np. arange(1,21,2) 
# print("range with step:",e)




# e= np. linspace(1,10,3)       #linspace( generates a specified number of evenly spaced value)
# print("linspace:",e)




# a= np.array([10,20,30,40])     #one dimentional and two dimentional arrays
# b= np.array([ [10,20,30], [40,50,60]])
# print("1d array:")
# print(a)


# print("2d arry:")
# print(b)


# print("dimensions:",a.ndim)
# print("shape:",a .shape)
# print("total elements :",a.size)

# print("dimensions:",b.ndim)
# print("shape:",b.shape)
# print("total elements :",b.size)



# a =np.array([10,2,30])
# b= np.array([1.5,2.5,3.5])
# c=np.array([True,False,True])
# z=np.zeros(5)
# print(a.dtype)
# print(b.dtype)
# print(c.dtype)



marks = np.array([75,82,68,91,88])          #acces array elements using indexing
print("first mark:",marks[0])
print("thrid mark:",marks[2])
print("last mark:",marks[-1])


marks[1] =95

print("updated marks:",marks)

            