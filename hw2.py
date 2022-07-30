# text= '''Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colourful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next programme in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colourless.
# But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money.'''
# print("количество s",text.count("s"))
# print("количество t",text.count("t"))
# len=len(text)-1
# a=1
# while a>0:
#     print(text.find("advert",a,len))
#     a=text.find("advert",a,len)+1
#     print(text[a-1:a+5].upper())


#2
# text=str(input("введите сторку ="))
# len=len(text)
# mid=len//2
# print(text[mid-1:mid+2])

#3
str_1=str(input("введите строку= "))
str_2=str(input("введите строку= "))
len=len(str_1)
a=0
str_3=""
while a<len:
    str_3+=str_1[a]+str_2[a]
    a+=1
print(str_3)
