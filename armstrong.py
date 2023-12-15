# sumfact = 0
# num = int(input("num: "))
# temp = num
# while(num):
#     i = 1
#     fact = 1
#     digit = num % 10
#     while(i <= digit):
#             fact = fact * i
#             i = i + 1
#     sumfact = sumfact + fact
#     num = num // 10
# if(sumfact == temp):
#     print("strong number")
# else:
#     print("not a strong number")

# num = int(input("num: "))
# s = 0
# li = []
# for i in range(1,num):
#     if num%i == 0:
#         s+=i
#         li+=[i]

# print("factors:",li)
# print("sum:",s)  
# if s == num:
#     print("perfect") 
# elif s>num:
#     print("abundant")
# else:
#     print("defecient")

n = int(input("n: "))
length=len(str(n))
s=0
temp=n
while temp > 0:
    dig=temp%10
    s+=dig**length
    temp=temp//10

print("sum of powers:",s)
if s==n:
    print("armstrong number")
else:
    print("not armstrong number")
    