print("hello world")
#asking for name, removing whitespace and capitalizing first letter  
name = input ("whats your name? ").strip().title()
#concatenation
print ("hello, " + name)
print("hello,",name)
#seperating 2 strings
print("hello,", name, sep='yo')  
#using ""inside a function
print ("hello, \"friend\"")
#special string 
print(f"hello,{name}")
#split users name into first and last name 
first, last = name.split()
print ("hello," , last)




