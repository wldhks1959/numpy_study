import numpy as np
# 특정 범위의 값을 가지는 N차원 배열 생성하기 
lst = list(range(0,9,2))
# print(lst)

arr = np.arange(9)
# print(arr)
# arr = np.arange(3,12)
arr = np.arange(stop=9, step=2, start=0) # (0, 9, 2)
# print(arr)

# np.linspace()
arr = np.linspace(0,100,11) # 0부터 100까지 원소가 균등하게 반환 
# print(arr)

# np.logspace()

arr = np.linspace(1,10,10)
print(arr, end="\n\n")

arr = np.logspace(1,10,10,base=2)
print(arr)

arr = np.logspace(1,10,10)
print(arr)