# # lambda[argument]:func body
# msg=lambda: print("hello")
# msg()

# def msg():
#     print("hello")
# var1=msg
# var1()
# print(msg)
# print(var1)

# square=lambda n:n*n
# print(square(4))
# sum=lambda a,b:a+b
# print(sum(4,4))

# def do_operation(a,b,operation):
#     result=operation(a,b)
#     print(f"result={result}")
# multiply=lambda a,b:a*b
# sum=lambda a,b:a+b
# do_operation(5,4,multiply)
# do_operation(5,4,sum)
# do_operation(5,4,lambda a,b:a-b)

# #взрыв мозга
# def select_operation(choice):
#     if choice==1:
#         return lambda a,b:a+b
#     elif choice==2:
#         return lambda a,b:a-b
#     else:
#         return lambda a,b:a*b
# operation=select_operation(1)
# print(operation(2,3))
# operation=select_operation(2)
# print(operation(2,3))
# operation=select_operation(3)
# print(operation(2,3))
#функ. внутри функ.
# def test():
#     def test2():
#         print("hello")
#     test2()
# test()
#заполненние списка /второй способ
# a=[i for i in range(1,15)] #генератор
# print(a)
#первый способ
# for i in range(1,16):
#     a.append(i)
# print(a)

# a=[2,-2,4,-4,7,5,12,23,-9]
# b=[i**2 for i in a if i>0 ]
# b=[i**2 if i>0 else i for i in a]
# b=[]
# for i in a:
#     b.append(i**2)
# print(b)


#обработка ошибок
'''
try:
    seeting
expect:
    setting

'''
# try:
#     number=int(input("Enter number: "))
#     number2=int(input("Enter number: "))
#     if number2==0:
#         raise Exception("second number must be biger than 0")
#     print(number/number2)
# except ValueError as v:
#     print("Value Error",v)
# except ZeroDivisionError as z:
#     print("Zero",z)
# except BaseException as b:
#     print("base error",b)
# except Exception as e:
#     print("My exeption ",e)
# finally:
#     print("program end")
# print("how are you")


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






