# myfile=open("test.txt","r")
# print(myfile)
# myfile.close()

#запись в файл
# try:
#     somefile=open("test.txt","a")
#     try:
#         somefile.write("hello world")
#     except Exception as e:
#         print(e)
#     finally:
#         somefile.close()
#         print("Finaly")
#
# except Exception as ex:
#     print(ex)

# with open("test.txt","a") as somefile:
#     # somefile.write("\tHello world ")
#     print("hello world",file=somefile)

#чтенние файла
with open("test.txt","r",encoding="UTF=8") as file:
    # for line in file:
    #     print(line,end="\n")
    ''''''
    # str1=file.readline(2)
    # print(str1,end="")
    # str2=file.readline(2)
    # print(str2,end="")
    ''''''
    # line=file.readline()
    # while line:
    #     print(line,end="")
    #     line=file.readline()
    ''''''
    # content=file.read()
    # print(content)
    ''''''
    # content=file.readlines()
    # print(content)
    ''''''
    # text=file.read()
    # print(text)
#пример
# FILENAME="msg8.txt"
# msgs=[]
# for i in range(4):
#     msg=input(f"введите строку {i}: ")
#     msgs.append(msg+"\n")
#
# with open(FILENAME,"a") as file:
#     for msg in msgs:
#         file.write(msg)
#
# with open(FILENAME) as file:
#     for msg in file:
#         print(msg,end="")

#
import csv
FILENAME="users8.csv"
users=[
    ["Tom",28],
    ["Alice",23],
    ["Bob",34]
]
with open(FILENAME,"w",newline="") as file:
    writer=csv.writer(file)
    writer.writerows(users)

with open(FILENAME,"a",newline="") as file:
    user=["Sam",21]
    writer=csv.writer(file)
    writer.writerow(user)

with open(FILENAME,"r",newline="") as file:
    reader=csv.reader(file)
    for row in reader:
        print(f"{row[0]} - {row[1]}")


