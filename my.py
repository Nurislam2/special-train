# import random
# size=int(input("введите размер массива = "))
# arr=[]
# for i in range(1,size+1):
#     arr.append(random.randint(0,size))
# for i in range(1,size):
#     buff=arr[i]
#     j=i-1
#     while j >= 0 and arr[j] > buff:
#         arr[j + 1] = arr[j]
#         j -= 1
#     arr[j + 1] = buff
# l=0
# r=size-1
# key=int(input("введите ключ= "))
# flag=False
# while (l<=r)and flag!=True:
#     mid=(l+r)//2
#     if arr[mid]==key:
#         flag=True
#         break
#     else:
#         if arr[mid]>key:
#             r=mid-1
#         else:
#             l=mid+1
# if flag==True:
#     print("индекс элемента",key," в массиве равен:",mid)
# else:
#     print("такого элемента нет в массиве")
#
