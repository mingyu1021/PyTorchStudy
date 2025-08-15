import matplotlib.pyplot as plt

plt.title('test')
plt.plot([1,2,3,4],[2,4,8,2])
plt.plot([1.5,2.5,3.5,4.5],[3,5,8,10])
plt.xlabel('hours')
plt.ylabel('score')
# 범례 삽입
plt.legend(['A student', 'B student'])
plt.show()