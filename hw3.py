#1
# data=[]
# num=int(input("введите число "))
# while num!=0:
#     data.append(num)
#     num = int(input("введите число "))
# data.sort()
# data.reverse()
# print(data)
# for i in data:
#     print(i)

#2
# i=0
# data=[]
# str_1=str(input("введите слово "))
# while str_1!="":
#     data.append(str_1)
#     str_1 = str(input("введите слово "))
# while i < len(data):
#     j = i+1
#     while j < len(data):
#         if data[i] == data[j]:
#             del(data[j])
#         j += 1
#     i += 1
# print(data)
# for i in data:
#     print(i)

#Доп. задание
data=[]
num=input("введите число ")
while num!="":
    data.append(num)
    num = input("введите число ")
data = [int(x) for x in data]
for i in data:
    if i<0:
        print(i)
for i in data:
    if i==0:
        print(i)
for i in data:
    if i>0:
        print(i)