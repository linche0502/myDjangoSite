
funs= []

for i in range(3):
    def fun():
        # global i
        # i= 0, 1, 2
        print(i)
    funs.append(fun)

for fun in funs:
    print(fun)
    fun()

print('======')




# def sum1(count, numList=[0,1]):
#     if count:
#         return sum1(count-1, numList+[numList[0-2]+ numList[-1]])
#     else:
#         return numList
# print(sum1(20))
# 
# 
# nums= [0,1]
# for i in range(20):
#     nums.append(nums[-1]+nums[-2])
# print(nums)

