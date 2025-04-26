#part 1
#1.true 
#2.true
#3.false
#4.false
#5.true

#part 2 
#1. 10 <= x <= 20
#2. len(s) > 0 "py" in s 
#3. n < 0 or abs(n) > 100 
#4. (user_role == "admin" and active) or superuser 
#5. not (temperature < 0 or temperature > 35)

#part 3
age = int(input("Enter your age: "))    
if age <= 0:
    print("Invalid age.")
    exit()
else:   
    print("You are an eligible.")

has_ticket = input("Do you have a ticket? (yes/no): ").lower()
vip_code = input("Enter VIP code(leave blanke if no code): ")

eligible = (age >= 18 and has_ticket == "yes") or (has_ticket == "no" and vip_code == "GOLDVIP")
print("\nAccess granted: <eligible> ")
   
#part 4
username = input("Enter your username: ")
password = input("Enter your password: ") 
email = input("Enter your email: ") 

if len(username) and len(password) >= 8 and any(char.isdigit() for char in password) and email.count("@") == 1 and email.endswith(".com"): 
    print("Form Valid.")
else:
    print("Form Invalid.")  

#part 5
    
order_amount = float(input("Enter order amount: "))
customer_type = input("Enter customer type (regular/member/vip): ").lower()
coupon_code = input("Enter coupon code (if any): ").strip()

total = order_amount

if order_amount < 50:
    total += order_amount * 0.05

if customer_type in ["member", "vip"]:
    total -= order_amount * 0.10

if customer_type == "vip" and coupon_code == "SAVE15":
    total -= order_amount * 0.15

print(f"Final total: ${round(total, 2)}")   