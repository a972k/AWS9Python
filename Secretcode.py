#assigment 1 
code1 = input().lower() # input function
code2 = input().lower() # input function
code3 = input().lower() # input function
numA = int(input()) # input function        
numB = int(input()) # input function

#assigment 2
if not (code1.isalpha() and code2.isalpha() and code3.isalpha()):
    print("Invalid codeword")
    exit() 
elif numA < 1 or numB < 1:
    print("Invalid numbers")
    exit()
    
#assigment 3
combine = code1 + "-" + code2 + "-" + code3    
secretnumber = (numA * numB) + numA - numB
numA, numB = numB, numA 
swappedA = numA
swappedB = numB
avg_value = (numA + numB) / 2
message_length = len(combine)
is_palindrome = combine.replace("-", "") == combine.replace("-", "")[::-1]

#assigment 4
print("Secret code: ", combine)
print("Secret number: ", secretnumber)
print("swapped values: ", swappedA, swappedB)
print("Average of originals: ", avg_value)
print("combined length: ", message_length)
print("palindrome: ", is_palindrome)