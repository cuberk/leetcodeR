
import time
import numpy as np
from matplotlib import pyplot as plt

# 递归实现
def fibRecursive(N: int) -> int:
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return fibRecursive(N - 1) + fibRecursive(N - 2)

# 用数组累加
def fibList(N: int) -> int:
    flist = [0, 1]
    tmp = N
    while tmp > 1:
        flist.append(flist[-1] + flist[-2])
        tmp -= 1
    return flist[N]


# n = int(input('输入'))
# start = time.time()
# print("递归结果：", fibRecursive(n))
# print("花费时间：", time.time() - start)
# start = time.time()
# print("数组累加结果：", fibList(n))
# print("花费时间：", time.time() - start)


time_record = []
for i in range(30):
    start = time.time()
    fibRecursive(i)
    time_record.append(time.time()-start)
# for i in range(30):
#     start = time.time()
#     fibList(1000*i)
#     time_record.append(time.time()-start)

x = np.arange(1, 31)
y = np.array(time_record)

plt.title("递归解斐波那契数时间")
plt.xlabel('斐波那契数序数')
plt.ylabel('花费时间')
plt.plot(x, y, "ob")
plt.show()