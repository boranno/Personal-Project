

import numpy  as np

'''

mat4x3=np.zeros((4,3))
mat4x3[0]=np.linspace(1,30,3)
mat4x3[2]=np.linspace(1,30,3)

print(mat4x3.shape)

mat3x4=mat4x3.reshape(3,4)

print(mat3x4.shape)
mat2to4=mat3x4[:,1:4]
print(mat3x4)
print(mat2to4.mean(axis=0))
print(mat2to4.max(axis=0))
print(mat2to4.var(axis=0))

'''

'''
arr=np.arange(0,30).reshape(5,6)
atp=np.transpose(arr)



print(arr)
print(atp)

'''

"""
arr=np.array([ i for i in range (0,20)]).reshape(2,10)
arr1=arr[:,3:6].copy()
arr1[0][1]=arr1[0][1]*5
print(arr1)

"""


'''

arr=np.array([x for x in range (0,100)]).reshape(10,10)
print(arr)
print(arr.sum(axis=0))
'''
'''
num_list=[x for x in range(100)]
nparay=np.array(num_list).reshape(10,10)
print(nparay.sum())
'''

arr=np.array([[x  for x in range(1,10)],[y for y in range(11,20)]])
print(arr)
arr2=arr.transpose()
print(arr2)



