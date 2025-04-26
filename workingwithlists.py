numbers_list = [3, 6, 8, 9, 12, 14, 17, 18, 30, 35]

numbers_list.append(36)

if 5 in numbers_list:
    numbers_list.remove(5)
else:
    print("5 not found in the list")    
    
numbers_list.insert(2, 2)
print(f"\nnew list: {numbers_list}")

sum_of_numbers = sum(numbers_list)
print(f"\nsum of numbers in the list: {sum_of_numbers}")

largest_number = max(numbers_list)
print(f"\nlargest number in the list: {largest_number}")
smallest_number = min(numbers_list)
print(f"\nsmallest number in the list: {smallest_number}")  