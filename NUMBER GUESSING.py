import random
secret_num= random.randint(1,100)
attempts = 1
guess=int(input("GUESS A NUMBER FROM 1 TO 100:"))
while guess != secret_num:
    if guess>secret_num:
        print("TOO HIGH")
    elif guess<secret_num:
        print("TOO LOW")
    attempts += 1

    guess = int(input("TRY AGAIN: "))

print("CORRECT!")
print("YOU GUESSED IT IN", attempts, "ATTEMPTS")
