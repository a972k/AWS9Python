import random
number = random.randint(1, 10)
geuss = int(input("guess a number between 1 and 10: ")) 
while geuss != number:
    if geuss < number:
        print("guess to low")
    else:
        print("guess to high")
    geuss = int(input("guess a number between 1 and 10: "))
print("congratulations you guessed it")
    