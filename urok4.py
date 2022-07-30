# # tom=("Tom",23)
# # print(tom)
# #
# # bob=["bob",25]
# # print(bob)
# # bob=tuple(bob)
# # print(len(bob))
# # listOfUsers=("anna","mallink","tom")
# # print(listOfUsers[1:3])
# # listOfUsers="hello"
# # print(listOfUsers)
# # name,age,company,position=("Tom",25,"Google","developer")
# # print(name,)
# # tom[0]="jery"
# # print(tom)
#
# # dictionary={
# #     "username":"Bekbolot3204",
# #     "password":"qwerty1234"
# # }
# # print(dictionary["username"])
#
# user_list=[
#     ["+13431","Bob"],
#     ["+13431", "Tom"],
#     ["+13431", "Anna"],
#     ["+13431", "Alice"],
# ]
# user_dist=dict(user_list)
# print(user_dist)
#
# # users_tuple=(
# #     ("+12621","Tom"),
# #     ("+12421", "bom"),
# #     ("+1211", "bob")
# # )
# # users_tuplE=dict(users_tuple)
# # print(users_tuplE)
#
users={
    "111":"Bob",
    "112":"Tom"
}
print(type(users))
# # # print(users["112"])
# # users["112"]="nub"
# # users["333"]="Anna"
# # user1=users.get("111","unknow users")
# # user2=users.get("444", "unknow users")
#
# # print(user1)
# # print(user2)
# # user_list=["qweq","qweq","eqwe"]
# # del (user_list[0])
# # print(user_list)
# # del users["111"]
# # print(users)
# # print(users)
# # user=users["555"]
# # # print(user)
# # key="555"
# # if key in users:
# #     user=users[key]
# #     print(user)
# #  else:print("Element not found")
# # user4 = users.pop("111","error")
# # print(user4)
# # #users.clear()
# # # print(users)
# users2=users.copy()
# # print(users)
# users2["555"]="qwer"
# # print(users2)
# #
# # users3={"+777":"Beka","+888":"Tima"}
# # users2.update(users3)
# # print(users2)
#
# # for key in users2:
# #     print(f"phone:{key},name: {users2[key]}")
# #
# # for key,value in users2.items():
# #     print(f"phone:{key},name: {value}")
# # for key in users2.keys():
# #     print(key)
# #
# # for value in users2.values():
# #     print(value)
# # print(users2.keys())
# # print(users2.values())
#
# users3={
#     "uuljan":{
#         "age":23,
#         "email":"uuljan@gmail.com",
#         "phone":"=055523234",
#     },
#     "Tima":{
#         "age": 23,
#         "email": "Tima@gmail.com",
#         "phone": "=055569586",
#         "is_married": True
#     },
#     "ulan":{
#         "age": 23,
#         "email": "ulan@gmail.com",
#         "phone": "=0555482048",
#         "is_married":True
#     }
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# }
# # print(users3["uuljan"]["age"])
#
# print(users3["uuljan"].get("is_married","Not"))
# users3["nuris"]={
#     "age": 23,
#     "email": "ulan@gmail.com",
#     "phone": "=0555482048",
#     "is_married":True
# }
# users3["uuljan"]["is_married"]=True
# del users3["Tima"]["is_married"]
# print(users3)
#
# users3["Tima"]["is_married"]=False
# for key,value in users2.items():
#      print(f"phone:{key},name: {value}")
# print(users3)
# for key in users3:
#      print(f"Name:{key},\n\tage: {users3[key]['age']},\n\temail:{users3[key]['email']},\n\tphone:{users3[key]['phone']},\n\tis_married:{users3[key]['is_married']}")
