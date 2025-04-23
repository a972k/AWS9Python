user_input = input("enter your number please,if you want to quit enter exit:")

number = int(user_input)
      
if number % 2 == 1:
    print("odd")       
else:
    print("even") 

try:
    number = int(user_input)
except ValueError:
    print("not a number")
    
    