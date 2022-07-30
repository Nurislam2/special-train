# def function(num):
#     list=[]
#     for i in range(1,num//2+1):
#         if num%i==0:
#             list.append(i)
#     list.append(num)
#     return list
#
# num=int(input("введите число= "))
# print("делители",function(num))

# data=[]
# lesser=[]
# bigger=[]
# summ=0
# num=input("введите число ")
# while num!="":
#     data.append(num)
#     num = input("введите число ")
# data=[int(i) for i in data]
# for i in range(0,len(data)):
#     summ+=int(data[i])
# summ/=len(data)
# print(summ)
# for i in data:
#     if i==summ or i<summ:
#         lesser.append(i)
#     else:
#         bigger.append(i)
#
# print("меньшее или равное среднему ",lesser)
# print("большее среднего",bigger)