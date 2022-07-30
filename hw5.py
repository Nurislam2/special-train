def function(a,b):
        return (a**2 + b**2)**1/2
a = int(input("кетет а="))
b = int(input("катет b="))
while a<=0 and b<=0:
    print("введите число больше нуля")
    a = int(input("кетет а="))
    b = int(input("катет b="))
c=function(a,b)
print(f"гипотенуза={c}")

# users={
#     1:"Bob",
#     2:"Tom",
#     3:"jerry",
#     4:"Luis"
# }
# def reverseLookup(key,dict):
#     return dict.get(key,"Not found")
#
# print(reverseLookup(2,users))