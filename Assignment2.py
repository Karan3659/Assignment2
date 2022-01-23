#Q1
print ('                  Question1 ')
string= 'Python is a case sensitive language. '
length = len(string)                              #length 1
print ('Length of string is' , length )
reverse= string [ ::-1]
print ('Reverse of the string is' , reverse)       #reverse (ii)   
b=string [9:26]                                    #store (iii)
string_2= string.replace("a case sensitive" , "object oriented")         
print ("Edited string is", string_2)                 #replace (iv)
index = string.find('a')
print (index)
no_white_space = string.replace(" ","")
print (no_white_space)                            #no white spaces (v)




#Question2
print ("    \n\n\n         Question 2")
name = input("Enter your name")
sid = int(input("Enter your sid"))
department_name=input("Enter your department name")
cgpa=float(input("Enter your cgpa"))
print ("Hey, %s Here!"%name)
print ("My SID is %d"%sid)
print ("I am from %s department and my CGPA is %f" %(department_name,cgpa))




#Question3
print ("    \n\n\n         Question 3")
a=56
b=10
print ("a&b equals %d" %(a&b))
print ("a|b equals %d" %(a|b))
print ("a^b equals %d" %(a^b))
print ("a<<2 equals %d" %(a<<2))
print ("b<<2 equals %d" %(b<<2))
print ("a>>2 equals %d" %(a>>2))
print ("a>>4 equals %d" %(a>>4))





#Question4
print ("     \n\n\n        Question 4")
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))
if (num1==num2==num3) :
    print ("The greatest number is %d" %num1)
elif (num1>=num2) :
    if num1>num3 :
        print ("The greatest number %d"%num1)
    else :
        print ("The greatest number is %d"%num3)
elif (num2>=num1) :
    if (num2>num3) :
        print ("The greatest number is %d" %num2)
    else :
        print ("The greatest number is %d"%num3)




#Question5
print ("       \n\n\n       Question 5")
if "name" in input("Enter the string : ") :
    print ("Yes")
else :
    print ("No")




#Question6
print ("        \n\n\n      Question 6")
x=int(input("Enter the length of the first side"))
y=int(input("Enter the length of the second side"))
z=int(input("Enter the length of the third side"))
if (x+y>z) and (y+z>x) and (x+z>y) :
    print ("Yes")
else :
    print ("No")
                
