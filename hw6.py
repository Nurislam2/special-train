 # def Prime_number(n):
#     d = 2
#     while n % d != 0:
#         d += 1
#     return d == n
# num=int(input("введите число "))
# print(Prime_number(num))

def function(*fruct):
    t=0
    b=""
    for i in fruct:
        t+=1
        if t==len(fruct):
            b+=f"и {i}"
        else:
            b+=f"{i},"
    print(b)
function("dd","ff","ff")
