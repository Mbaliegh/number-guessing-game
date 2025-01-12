#Number guessing
import random


print("Welcome to the Number Guessing Game!\n")

print("Please select the difficulty level\n"
      "1. Easy (10 chances)\n"
      "2. Medium (5 chances)\n"
      "3. Hard (3 chances)\n")

while True:
    count = 0
    difficulty = 0
    numb_rand = random.randint(1, 100)
    while True:
        try:
            user = int(input("Enter your choice: "))

            if user == 1:
                difficulty=10
                print("Great! You have selected the Easy difficulty level.")
                break
            elif user == 2:
                difficulty=5
                print("Great! You have selected the Medium difficulty level.")
                break
            elif user == 3:
                difficulty=3
                print("Great! You have selected the Hard difficulty level.")
                break
            else:
                print("Please select 1,2 or 3")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3")

    print("Let's start the game\n")

    for chances in range(difficulty):
        count+=1

        try:
            user_numb= int(input("Enter your guess (1-100): "))
            if user_numb<1 or user_numb >100:
                print("Input is out of bound.Please enter a number between 1 and 100")
            elif user_numb==numb_rand:
                print(f"Congratulations! You guessed the correct number in {count} attempts")
                break
            elif user_numb > numb_rand:
                print(f"Incorrect! The number is less than {user_numb}")
            elif user_numb< numb_rand :
                print (f"Incorrect!! The number is greater than {user_numb} ")
        except ValueError:
            print("Input must be a number between 1 and 100")
    else:
        print(f"Game over !! The correct number is {numb_rand}")

    conti = input("Do you want to play again? Enter 'y' for Yes or any other key to Exit: ").lower()
    if conti == "y":
        continue
    else:
        print("Thank you for playing!")
        break
