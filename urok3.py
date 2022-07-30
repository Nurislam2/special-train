# num=[1,2,3,4,5]
# print(num)
# people=["sam","Tom","bob"] * 3
# print(people)
# print(len(people))
# object=[1,2.1,"hello",True]
# print(object)
# msh="hello"
# msg=list(msh)
# print(msg)
# people=["sam","Tom","bob"]
# print(people[0])
#  print(people[-1])
# people[1]="qwer"
# print(people)
# people=["sam","Tom","bob"]
# tom,bob,sam=people
# print(tom)
# print(bob)
# print(sam)
# people = ["sam" , "Tom" , "bob"]
# for person in people:
#     if person=="Tom":
#         #continue
#         #break
#         pass
#     print(person)
# i=0
# while i<len(people):
#     print(people[i])
#     i+=1
#
# object=[2,3.5,"abu",True,False,25,3.51,"hello"]
# int_List=[]
# str_list=[]
# float_List=[]
# bool_List=[]
# object.remove(False)
# k=0
# for i in object:
#     if isinstance(i,int) and not isinstance(i,bool):
#         int_List.append(i)
#     elif isinstance(i,str):
#         str_list.append(i)
#     elif isinstance(i,float):
#         float_List.append(i)
#     else:
#         object.remove(i)
#
# str_list.append("Err")
# str_list.append("Crr")
# str_list.append("Crr")
# str_list.append("Drr")
# int_List2=[11,33,2,5,1,6]
# int_List2.sort()
# str_list.sort()
# str_list.reverse()
# print(str_list[::-1])
# str="acbd"
# print(str[::-1])
# print(int_List2)
# print(int_List)
# print(str_list)
# print(str_list.count("Crr"))
# print(float_List)
# print(object)
# object=[2,3.5,"abu",True,False,25,3.51,"hello","343"]
# object2=object.copy()
# object2.append("Hello")
# print(object.pop(4))
# object.pop(4)
# print(object)
# print(object2)
# print(max([12,14,222,432,95]))
# print(min([12,14,222,432,95]))
#
# people=["sam","Tom","bob","Alice"]
# nums=[1,2,3,4,5]
#
# if "Alice" in people:
#     people.remove("Alice")
# print(people)
# res=people+nums
# print(res)
# print(sorted(list("4321")))
# i=0
# lis=[]
# while True:
#     i=int(input("число= "))
#     if i==0:
#         break
#     lis.append(i)
#     lis.sort()
#
# while i<len(lis):
#     print(lis[i])
#     i+=1

data=[]
num=int(input("введите число "))
while num!=0:
    data.append(num)
    num = int(input("введите число "))
data.sort()
print(data)
for i in data:
    print(i)



