""" numpy"""
"""It is a ipen source python library used for scientific compputing applications
and it stands for numerical python which is consists of multidimensional array
objects and a collection of routines for processing it"""

"""list contains heterogeneous elements while
numpy array contains only hohmogeneous elements"""

"""Array"""

#creating 1-D array
import numpy as np
a1 = np.array([145,132,36,13])
print(a1)

#creating multidimensional array
a1 = np.array([[1,2,3,4],[5,6,7,8]])
print(a1)

#converting 1-D array to N-D array by using "ndmin=N"
a1 = np.array([1,2,3,4],ndmin=3)
print(a1)

#changing data type
a1 = np.array([1,2,3,4,5],dtype=complex)
print(a1)

#to find dimension of array
a1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a1.ndim)

#finding size of each item in array
a1 = np.array([1,2,3,4])
print("Each item contains in byte::",a1.itemsize)

#finding data type of each item
a1 = np.array([1,2,3,4])
print("Data type of each item::",a1.dtype)

#to check size and shape of array
a1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Size of array::",a1.size)
print("Shape of array::",a1.shape)

#create a sequence of integers using arrange
#arange(sratr,end,step)
a1 = np.arange(0,20,2)
print(a1)

#create array upto n from zero by using arange(n)
a1 = np.arange(11)
print(a1)

#accesing particular element
a1 = np.arange(11)
print(a1[2])
print(a1[-2])

#access array elements using slicing
a1 = np.arange(10)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a2 = a1[1:8:2]
print(a2)
#[1 3 5 7]
a2 = a1[-2:3:-1]
print(a2)
#[8 7 6 5 4]
a2 = a1[-2:10]
print(a2)
#[8 9]


#multi dimension array
a1 = np.array([[1,2,3,4],[5,6,7,8]])
print(a1.shape)
print(a1.size)

#accessing elemets
print(a1[1,1])#6
print(a1[0,0])#1
print(a1[1,-1])#8



#slicing
a1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a1)
#a1[row(start:end),col(start:end)]
print(a1[1,2])
print(a1[:,1])
print(a1[1,:])

a2 = a1[1:,2:]
print(a2)


#creating 2-d array by generating sequence 
a1 = np.arange(35).reshape(5,7)
print(a1)

#boolean array indexing
a1 = np.arange(12).reshape(3,4)
print(a1)
rows = [False,False,True]
wanted_rows = a1[rows,:]
print(wanted_rows)


#convert numpy array to python list
#1-D array
a1 = np.arange(11)
print("Array::",a1)
print(type(a1))
#<class 'numpy.ndarray'>
l1 = a1.tolist() #convert to list
print("List::",l1)
print(type(l1))
#<class 'list'>

#multi-D array
a1 = np.arange(12).reshape(3,4)
print("Array::",a1)
print(type(a1))
#<class 'numpy.ndarray'>
l1 = a1.tolist() #convert to list
print("List::",l1)
print(type(l1))
#<class 'list'>



#convert python list into numpy array
l1 = [1,2,3,4,5,6]
a1 = np.array(l1)
a2 = np.asarray(l1)
print(a1)
print(a2)
print(type(a1))#<class 'numpy.ndarray'>
print(type(a2))#<class 'numpy.ndarray'>

#reshaping array
a1 = np.array([[1,2,3,4],[5,6,7,8]])
print(a1.shape)

a1.shape=(4,2)
print(a1)
print(a1.shape)
'''or'''
a2 = a1.reshape(4,2)
print(a2)
print(a2.shape)

"""numpy application
fourier transform and shape manipulation
mathematical and logical operations
Linear algebra and Random number generation"""