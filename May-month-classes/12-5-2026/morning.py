# loops


# name = "python"
# for i in range(name):
#     print(i)
    
    
# this is an error becouse we have to paas numerical values in the range not a string or anything 
    
    #traversing of string using range 
    
# name = "python programing"    
# size = len(name)
# for i in range(size):
#     print(name[i],i)
    
    
    
    
# in this program se are string the len of the variable in the size variable than printing the name varaible in the last

# 2. traversing the string wothout using range 

# name = "karan"
# for i in name:
#     print(i)

# 3. the cool method 

# for i in "python":
#     print(i)    
    
    
# wap to count all the vovesls for the given string 

# name = " this is devops batch"
# vovl = 0
# con = 0



# wap to print your name in reverce formate 
# name = "kaushal"
# rev = ""
# for i in name:
#     rev = i + rev
# print(rev)    
    
    
# name = "PYTHON"
# size = len(name)
# for i in range(size):
#     print(name[i],name,i)
   
   
# wap to sum of the indices fo the string "python"

# name = "python"   
# size = len(name)
# sum = 0
# for i in range(size):
#     sum += i
#     print(sum)

# wap to print sum form 1 to 8


# sum= 0 
# for i in range(9):
#     sum += i
#     print(sum)
    
    
# WAP to print prime number form 1 to 15

for num in range(1, 16):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
              break
        else:
            print(num)
        
        
    
    
    