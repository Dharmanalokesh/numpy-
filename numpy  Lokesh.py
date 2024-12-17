'''ndim = dimensions'''
# import numpy as np
# arr1 = np.array(([1],[2]))
# print(arr1)
# print(arr1.ndim )

# import numpy as np
# arr2 = np.arange(1, 12,3)
# arr3 = np.linspace(1,5,3,endpoint=False)
# print(arr2.ndim) 
# print(arr2)      
# print(arr3.ndim) 
# print(arr3)     

'''diag=diagnol matrix'''

# import numpy as np
# arr3=np.eye(4,4,3)
# arr4 =np.diag([1,2,3,4],2)     
# arr5=np. 
# print(arr3.ndim)
# print(arr3)
# print(arr4.ndim)   
# print(arr4)

'''3D'''
# import numpy as np 
# b=np.array([[[1,2],[2,3],[3,4],[4,5]]])
# print(b)
# print(b.ndim)

# import numpy as np
# a=np.array([[1,2,3],
#             [5,6,7]])
# # print(a.shape)
# # print(a.ndim)
# # print(a.dtype)
# # print(a.itemsize)
# # print(a.nbytes)
# print(a[0,2]) #(r,c)
# print(a[0,:]) #(for getting rows)
# print(a[:,2]) #(for getting col)

''''for getting different methods'''
# import numpy as np
# j=np.zeros((2,7))
# l=np.ones((2,6))
# k=np.indices((3,3))
# # m=np.full((3,5),143)
# # m= np.random.rand(2, 3)
# # r=np.identity(6)
# # print(r)
# # print(k)
# # print(m)
# # print(j)
# # print(l)

''''copy method and number changing in a list '''
# import numpy as np
# a=np.array([1,2,3,4])
# b=a.copy()
# b[1]=5
# print(b)
# print(id(a))
# print(id(b))

'''mathematical operations'''
# import numpy as np
# a=np.array([1,2,3,4])
# print(a+2)
# print(a-2)
# print(a/2)
# print(a*5)
# print(a**2)   #powers 
# print(a**3)

'''21/10/24'''
# import numpy as np
# a=np.array([[1,2,3],
#             [5,6,7]])
# b=np.array([1])
# c=np.array([1])
# d=a[b,c]
# print(d)

# import numpy as np
# # a=np.array([1,2,3,4,5,6,7,8,])
# b=a>2
# c=a[b]
# print(c)
# print(id(a))

# import numpy as np
# a=np.array([[1,2,3,4,5],                  #doubt
#            [11,12,13,14,15]])
# b=a[0,2:1:3]
# print(a)


'''combining list of numbers by using for loop'''
# import numpy as np 
# a=np.array([[1,2,3,4,5,6,7,8,9],[11,12,13,14,15,16,17,18,19]])
# for i in a:
#     for j in i: 
#         print(j)


# import numpy as np 
# b=np.array([[[1,2,11],[2,3,12],[3,4,13],[4,5,14]]])
# c = b[0:2, 1:2, 1:2]
# print(c)
# print(c.ndim)

'''22/10/24'''
# import numpy as np
# a=([1,2,3])
# print(a)

