#set
# users={"Uuljan","Ulan","Tima","Ulan"}
# print(users)

# users_list=["Uuljan","Ulan","Tima","Ulan"]
# print(users_list)
# people=set(users_list)
# print(people)

# users=set()
# users.add("Sam")
# users.add("Erden")
# users.add("Tima")

# print(users)
# if "Sam" in users:
#     users.remove("Sam")
# print(users)

# users.discard("Tim")
# print(users)
# users.discard("Sam")
# print(users)

users={"Tom","Bob","Alice"}
# users2={"Sam","Tom","Bob","Alice","Greg"}
# users3=users.union(users2)
# users3=users.intersection(users2)
# users3=users&users2
# users3=users.difference(users2)
# users3=users2-users
# users3=users.symmetric_difference(users2)
# users3=users.issubset(users2)
# users3=users2.issubset(users)
# print(users3)

# users=frozenset(users)
# print(users)

#function

# def say_hello():print("hello")
# def say_goodbye():print("goodbye")

# say_hello()
# say_goodbye()

# def print_msg():
#     def say_hello(): print("hello")
#     def say_goodbye(): print("goodbye")
#     say_hello()
#     say_goodbye()
# print_msg()
#
# def main():
#     say_hello()
#     say_goodbay()
# def say_hello():
#     print("hello")
# def say_goodbay():
#     print("goodbay")
# main()
#
# def say_hello(name,age):
#     print(f"hello {name},{age}")
# say_hello("nuris",21)
# say_hello("ulan",21)
# # say_hello()
# say_hello(age=23,name="Tima")

#аркс *score
# def print_scores(student,*scores):
#     print(f"student name:{student}")
#     print(scores)
#     for score in scores:
#         print(score)
# print_scores("askar",2,2,4,1,4,1,4)
# a=[1,2,3]
# b=[*a,4,5,6]
# print(b)

# кваркс **subjects
def print_scores(student,*scores,**subjects):
    print(f"student name:{student}")
    print(type(scores))
    print(type(subjects))
    for score in scores:
        print(score)
    for k,v in subjects.items():
        print(f"{k}:{v}")
print_scores("askar",2,2,4,1,4,1,4,sub1="math",sub2="English",sub3="Geography")

#retrn
# def get_msg(msg):
#     return f"Msg:{msg}"
# a=get_msg("jdjd")
# print(a)
# print(get_msg("dada"))

# def sqrt(num):
#     return 2**num
# res1=sqrt(5)
# res2=sqrt(55)
# print(res1)
# print(res2)

# def print_person(name,age):
#     if age>120 or age <1:
#         print("invalid age")
#         return
#     print(f"name:{name} Age:{age}")
#
# print_person("nuris",20)
# print_person("nuris",-20)

