# Type Casting : The process of Converting a value from one data type to another (String, Integer, Float, boolean)
name = "cjricch"
age = 25
score = (7.5)
money = True

print(type(name))
print(type(age))
print(type(score))
print(type(money))


#How to convert a value to different data type

age = float(25)
print(age)

score = int(7.5)
print(score)

money = str(True)
print(money)

name = bool("cjricch")
print(name)

#                              Explicit vs Implicit
#                                    Explicit

#Explicit typecasting is manually converting a values or variable into a different data type by using one of these keywords above

#Explicit means something is stated directly and clearly — no guessing required.

#                                    Implicit

#Implicit typecasting is when a value or variable is converted into a different data type automatically

#Implicit means something is suggested, implied, or understood without being directly stated — you have to infer it from context.

x = 2
y = 2.0

x = x / y
print(x)
