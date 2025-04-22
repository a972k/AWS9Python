#dear teacher/checker please uncheck the need to run assignment 



#Exercise 1: Salary Breakdown 
#gross_salary = float(input("Enter your gross salary: ")) # Calculate deductions
#net_income = gross_salary - ( gross_salary * 0.22 )
#print("Your net income is", net_income)
#if net_income > 3000:
#    print("You have enough money for rent")
#else:
 #   print("You don't have enough money for rent")
#if net_income - 3000 > 1000:
 #   print("rent and save money")
#elif net_income - 3000 = 0:
 #   print("rent only")
#else:
 #   print("it not enough ")
 
     
#Exercise 2:  Shipping Calculator
#item = input("Enter the name of the item: ")
#item_price = float(input("Enter the price of the item: "))
#item_quantity = int(input("Enter the quantity of the item: "))
#item_total = item_price * item_quantity
#print("The total price of the item is", item_total)
#if item_total <= 200:
#    shipping_cost = item_total + 50
#else:
#    shipping_cost = item_total 
    #final_price = shipping_cost  
#if final_price > 500:
#    after_discount = final_price * 0.9      
#    print("The final price after discount is", after_discount)
#else:
#    print("no discount apllied The final price is", final_price)


#Exercise 3: Medieval Guard Duty
#age = int(input("enter your age"))
#black_list = input("black list yes/no").lower() == "yes"
#royal_family = input ("royal family yes/no").lower() == "yes"
#gold_pass = input("gold pass yes/no").lower() == "yes"
#if age >= 18 and not black_list and (royal_family or gold_pass):
#    print ("come in")
#else:
#     print ("go away")

    
#Exercise 4: Car Insurance Quote   
#driver_age = int(input("Enter your age: "))
#number_of_accidents = int(input("Enter the number of accidents: "))
#if driver_age < 25: 
#    premuim = 3000
#else:
#    premuim = 2000
#if number_of_accidents  == 0:
#       premuim = premuim + 0
#else:
#    premuim = premuim + 500 * number_of_accidents
#if premuim > 5000:
#    print("Your insurance is price is", premuim) 
#    print("you are a high risk driver")
#else:
#    print("Your insurance price is", premuim) 
#    print("you are a standard driver")

    
#Exercise 5:vab safety checklist
#temperature = int(input("Enter the temperature: "))
#pressure = int(input("Enter the pressure: "))
#voltage = int(input("Enter the voltage: "))
#if temperature >= 20 and temperature <= 80 and pressure < 50 and voltage > 200 and voltage < 250 :
#    print("safe to proceed")
#else:
#    print("unsafe conditions")


#Exercise 6: Wizard’s Final Exam
#print("you are under evaluation")
#Wizard = input("enter your name: ")
#print("Welcome", Wizard)
#spell_power = int(input("enter your spell power between 0 to 100: "))
#accuracy = int(input("enter your accuracy between 0 to 100: "))
#control = int(input("enter your control between 0 to 100: "))
#average = (spell_power + accuracy + control) / 3
#if average >= 90:
#    print(Wizard, "You are an Archmage")
#elif average >= 75 and average < 90:
#    print(Wizard, "You are a Mage")
#elif average >= 60 and average < 75:
#    print(Wizard, "You are an apprentice")
#elif average < 60:
#    print(Wizard, "You are a failure")