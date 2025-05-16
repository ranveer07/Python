# text = " \nhello world "

# text[0]= "R"    TypeError: 'str' object does not support item assignment  due to it is immutable
 
# print(text.upper())    #HELLO WORLD
# print(text.lower())    #hello world
# print(text.capitalize()) #Hello world
# print(text.title())      #Hello World  


# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())


# text = "Python is fun and fun is fun"

# print(text.find("is"))
# print(text.replace("fun", "awesome"))


# text = "Apples,Banana,Pineapple"

# print(text.split(","))
# print(",".join(['Apples', 'Banana', 'Pineapple']))



text = "Python123"
print(text.isalnum())  # true
print(text.isdigit())  #False
print(text.isalpha())  #False
print(text.isspace())  #False