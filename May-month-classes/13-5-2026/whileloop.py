   # while loop
# 1. initilizer
# 2. condition
# 3. incriment/decriment 

# to print sequance number in accending order
# i =1
# while i <= 10:
#     print(i,end=" ")   
#     i+=1
 
 
 # to print in decending order
 
# i = 10 
# while i>=1:
#     print(i)
#     i-=1

# wap to print all the vovels in the string

# str = "skncokdsn dvkdnvokndsv nkodnvkodsnv pjapojf"
# vovels = "aeiouAEIOU"
# count = 0
# consonent = 0
# i = 1
# while i < len(str):
#    if str[i] in vovels:
#       count +=1
#    else:
#       consonent +=1   
#    i +=1
# print(f"total vovels are {count}\n and the consonent are {consonent}")  




# wap to print total word count in the string



# str = "vmioaismv oasd pvmvmapsodpjmvm vnoinm xkn ok "
# i = 1
# count = 0
# while i < len(str):
#    count+=1
#    i+=1
# print(len(str))   
# print(count)    



# wap to print factorial of any number


# num = int(input("enter the number you want to find the factorial"))
# i = num
# fat = 1
# while i >1:
#    fat  *= i 
#    i-=1
# print(fat)   


# wap to print the table of any number

# num = int(input("enter the number you want to see the table of :"))
# i = 1
# while i <= 10:
#    print(f"{num} x {i} = {num*i}")
#    i+=1
      

      
# wap to print the sequance of cubes or the numbers


# num = int(input("Enter the number"))
# i = 1

# while i <= num:
#    print(f"the cube of the numbrers  {i} = {i*i*i}")
#    i += 


# str = "knsvdvkn6747jfnf47y3"
# c = 0
# c1 =0
# i = 1
# cam = "1234567890"
# while i < len(str):
#    if str[i] in cam:
#       c +=1
#    else:
#       c1+=1
#    i+=1
# print(c)
# print(c1)         
      

   
   
# wap to print tringle of star

# num = int(input("ente the number you want to print tringle :-"))
# i = 1
# while i <= num:
#    print("*",end="") 
#    print("*")
#    print("*",end=" ")
#    print("*")
#    i +=1        

#wap to print all the total of even numbers form 1 to 15.

# i = 1
# sum = 0
# num = 15
# while i <= num:
#    if i %2 ==0:
#       sum +=i
#    i+=1
# print(sum)    

# wap to chck the given string by the user is palandrom or now 


# str = input("enter the str")
# i = len(str)-1
# str1 = ""
# while i>=0:
#    str1 =str1 + str[i] 
#    i -=1
# if str1 == str:
#    print("palandrom")
# else:
#    print("not palandrom")      


  
  
# wap to erversr the digit "1234"
# num = 1234
# i= 10
# rev = 0
# while num >0:
#    digit = num % 10
#    rev = rev*10 +digit
#    num=num//10
   
# print(rev)   


# str = "aeioudkjncj"
# count = 0
# con = 0
# i = 0
# while i <len(str):
#    print(str[i])
#    if str[i] in "aeiou":
#       count +=1
#    else:
#       con+=1   
#    i+=1   
   
# print(count)
# print(con)   


num = int(input("enter the numebr "))
i = 0
while i <=10:
   print(f"{num}x{i}={num*i}")
   i+=1