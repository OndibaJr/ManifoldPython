#level1

#Day 2: 30Days of pyhton programming
firstName="Jason"
lastName="Martins"
fullName=firstName+" " +lastName
myCountry="Beulah"
myCity="Kanairo"
age="43"
thisYr=2025
is_married=True
is_true=False
is_light=False

print(firstName)
print(lastName)
print(fullName)
print(myCountry)
print(myCity)
print(age)
print(thisYr)
print(is_married)
print(is_true)
print(is_light)

a,b,c,d,e=10,20,30,40,50


#level 2

#typeof() function
print(type(firstName))
print(type(lastName))
print(type(fullName))
print(type(myCountry))
print(type(myCity))
print(type(age))
print(type(thisYr))
print(type(is_married))
print(type(is_true))
print(type(is_light))

#len() function
print(len(firstName))
len2=len(lastName) 
len1=len(firstName)

if(len1<len2):
    print("lastName is longer than firstName")
else:
    print("firstName is longer than lastName")

num_one=5
num_two=4
total=num_one+num_two
print("The sum of ",num_one," and ",num_two," is ",total)

diff=num_one-num_two
print("The difference between ",num_one," and ",num_two," is ",diff)

product=num_one*num_two
print("The product of ",num_one," and ",num_two," is ",product)

division=num_one/num_two
print("The division of ",num_one," and ",num_two," is ",division)

remainder=num_one%num_two
print("The remainder of ",num_one," and ",num_two," is ",remainder)

exp=num_one**num_two
print("The exponent of ",num_one," and ",num_two," is ",exp)

floor_division=num_one//num_two
print("The floor division of ",num_one," and ",num_two," is ",floor_division)


myRadius=30
pi=3.14
area_of_circle=pi*myRadius**2
print("The area of the circle is: ",area_of_circle)
circum_of_cirlce=2*pi*myRadius
print("The circumference of the circle is :",circum_of_cirlce)

#input function
r=input("Enter the radius of the circle: ")
radius2=int(r)
myArea=pi*int(radius2)**2
print("The area of the circle is: ",myArea)

fName=input("Enter your first name: ")
print("Your first name is: ", fName)
lName=input("Enter your last name: ")
print("Your last name is: ", lName)
country=input("Enter your country: ")
print("You are country is: ", country)
age=int(input("Enter your age: "))
print("You are age is: ", age)




