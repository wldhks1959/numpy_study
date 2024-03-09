import numpy as np
# 정해진 형식의 n차원 배열 생성 

# np.zeros()
arr = np.zeros([2,2])
# print(arr)

# np.ones()
arr = np.ones([3,7])
# print(arr)

# np.full()
arr = np.full((2,3), 5)
# print(arr)

# np.eye()
# arr=np.eye(3,4, k=0)
arr=np.eye(3)
# print(arr)

arr = np.array([[1,2,3],[4,5,6]])

# np.zeros_like()
arr_z = np.zeros_like(arr)
# print(arr_z)

# np.ones_like()
arr_o = np.ones_like(arr)
# print(arr_o)

# np.ones_like()
arr_f = np.full_like(arr, 3)
print(arr_f)