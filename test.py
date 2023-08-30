
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

print('===')

print(f'-{1 :05d}-')

compare= lambda a,b: print(a, b, a==b)
print('-拉丁系字母-')
compare('þ', 'b')
compare('ɑ', 'a')
compare('ᴄ', 'c')
compare('ᴏ', 'o')
print('-西里爾字母-')
compare('А', 'A')
compare('а', 'a')
compare('В', 'B')
compare('е', 'e')
compare('о', 'o')
compare('Р', 'P')
compare('р', 'p')
compare('С', 'C')
compare('с', 'c')
compare('х', 'x')
compare('ѡ', 'w')




import requests, json
import pandas as pd
response= requests.get('https://www.google.com.tw')
import re
text= response.text
text= re.sub('<script[\\s\\S]*?>[\\s\\S]*?<\\/script>', '', text)
text= re.sub('<style[\\s\\S]*?>[\\s\\S]*?<\\/style>', '', text)
text= re.sub('<[^>]*>','',text)
text= re.sub('\\s+','\n',text)
# print(text)



data= pd.read_csv('https://www.twse.com.tw/exchangeReport/STOCK_DAY_ALL?response=open_data')
# print(data)




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

