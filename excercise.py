

#Create a program that asks the user to 
#enter their name and their age.
# Print out a message addressed to them that 
#tells them the year that they will turn 100 years old.
# Note: for this exercise, 
# expectation is that you explicitly write out the year (and therefore be out of date the next year).
#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
#Print out that many copies of the previous message on separate lines. 
#(Hint: the string "\n is the same as pressing the ENTER button)
# Character Input

def character_input():
        name = input("Enter you Name :")
        age = int(input("Enter your age :"))
        current_year = 2023
        year_100 = current_year + (100 -age)
        mes = f"{name}, You will turn 100 years old in the year {year_100}.\n"
        print(mes)

# # Odd or Even #
# # Ask User for number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# # Hint : How des an even/Odd number react differently when divided by 2?
# # extras:
# # if the number is a multiple of 4, print out a different message.
# # Ask the user for two numbers: one number to check (call it num ) and one number to divide by(check).
# # if check divides evenly into num, tell that to the user. if not, print a different approriate message.
# # # concepts:
# #Modular arithmetic 
# # Conditionals(if statements)
# # Checking equality.

def odd_or_even():
        num = int(input("Enter a number : "))
        check = int(input("Enter a number to divide by {check} :"))
        if num %2 == 0 :
                print(f" Given {num} is even number ")
                if num % 4 == 0 :
                        print(f" Given {num} is multiple of 4.")
        else:
                print("{num} is odd number.")
        if num % check ==0 :
                print(f"{check} divides evenly into {num}")
        else:
                print(f" {check } does not divide evenly into {num}.")

# # List less than ten #
# # Create a list and write a program that prints out all elements of the list that are less than 5.
# # extras Instead of printing the elements ony by one , make a new list that has all the elements less than
# # 5 from the list in it and print out this new list.
# # wirte this in one line of python code .
# # ask the user for a number and return a list that contains only elements from the original list a that are smaller than the number given by the user.


def list_less_than_ten():
        list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20 , 25, 23 , 21, 19, 18 , 15, 51, 100, 100000]
        user_input = int(input("Elements a number "))
        new_list = [element for element in list if element < user_input]
        print(f"Elements less than {user_input}: ", new_list)
# Divisors#
# Create a program that asks user for a number and then prints out a list of all the divisors of that number. 
# Divisor is, it is a number that divides evenly into another number. For Example, 13 is a divisor of 26 because 26/13 has no remainder.

def find_divisors():
       num = int(input("Enter a number : "))
       divisors = [i for i in range (1, num+1) if num % i ==0]
       print(f"Divisors for the given number are {divisors}")
 

# List Overlap#
# two list and write program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure program works on two list of different sizes.
# extras Randomly generate two lists to test this
# write this one line python 
def list_overlap():
    list1 = [ 1, 1, 2, 3, 5, 8, 21, 34, 55, 89]
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 45]
    def combine(list1, list2):
        return list(set(list1) & set(list2))
    combine_elements = combine(list1, list2)
    print(f" These are the elements that are common in both the list: \n", combine_elements )


# Ask the user for a string and print out whether this string is a palindrome or nor (A palindrome is a string that reads the same forwards and backwards.)
#"madam","racecar","level","radar","civic","rotor","kayak","refer","deified", "noon"
def is_palindrome(s):
    return s == s[::-1]

def palindrome():
    user_input = input("Enter a string to check if it's a palindrome: ").lower().replace(" ", "")
    if is_palindrome(user_input):
        print("It's a palindrome.")
    else:
        print("It's not a palindrome.")

# list of Comprehensions 
# I give you list saved in a variable. Write one line of python that takes this list a and makes a new list that has only the even elements of this list in it.
def list_of_comprehensions():
    a =[1,4, 9, 16, 25, 36, 49, 64, 81, 100]
    even_number = [num for num in a if num % 2 == 0 ]
    print(f"These are the Even Numbers :\n",even_number)

# Rock paper Scissors
# Make a two player Rock paper scissors game. 
# hint Ask for a player plays using input, compare, print out a message of congratulatioons to the winner, and ask if the players want to start a new game.
# Remb 
# Rock beats scissors , Scissors beats paper , Paper beats rock 

def rock_paper_scissors():
    print("Pick any one: Rock, Paper, Scissors")
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}

    while True:
        player_a = input("Player A: ").lower()
        player_b = input("Player B: ").lower()

        if player_a not in game_dict or player_b not in game_dict:
            print("Invalid input! Please choose 'rock', 'paper', or 'scissors'")
            continue

        a = game_dict[player_a]
        b = game_dict[player_b]
        diff = a - b

        if diff in [-1, 2]:
            print('Player A wins.')
            if input("Do you want to play another game? (Y/N): ").lower() != 'y':
                print("Game Over.")
                break
        elif diff in [-2, 1]:
            print('Player B wins.')
            if input("Do you want to play another game? (Y/N): ").lower() != 'y':
                print("Game Over.")
                break
        else:
            print('Draw, Please Continue.')
            print('')
           

# Guessing Game One
# Generate a random number between 1 and 9 (including 1 and 9 .
#ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.)
# keep the game going untill user types exist.

def guess_the_number():
    import random
    random_number = random.randint(1, 9)
    guess_count = 0

    while True:
        user_input = input("Guess a number between 1 and 9 or type 'exit' to quit: ")

        if user_input.lower() == 'exit':
            print(f"You've exited the game. Total guesses: {guess_count}")
            break

        guess = int(user_input)
        guess_count += 1

        if guess < random_number:
            print("Your guess is too low.")
        elif guess > random_number:
            print("Your guess is too high.")
        else:
            print("Congratulations! You guessed it right!")
            print(f"It took you {guess_count} guesses.")
            break
               
# List Overlap Comprehensions
# take two list and write a program that returns a list that contains only the elements that are common between lists 

def List_overlap_comprehensions():
     import random
     a = random.sample(range(1,30),12)
     b = random.sample(range(1,30),16)
     result = [i for i in a if i in b]
     print(result)


# Check Primality Functions
# Ask User for a number and determine whether the number is prime or not.
# for those who have forgotten, a prime number is a number that has no divisors). 
# use functions, Resuable functions, Default arguments.

def primality_functions_solutions():
    import sys
    number = input("Please enter a number" + "\n" + ">>>")
    number = int(number)
    prime = False #initiate boolean for true false, default false
    if number > 0:
        for x in range (2, number - 1): #this range excludes number and 1, both of which number is divisible by
            if number % x != 0: #If number isn't evenly divisible by x, start over with the next one
                continue 
            elif number % x == 0: #If number is evenly divisible by x, it can't be prime
                sys.exit("The number is not prime.")
        sys.exit("The number is prime.") #number wasn't evenly divisible by any x, so it's prime
    elif number == 0:
        sys.exit("The number is not prime.") #According to the Google, 0 is not prime
    else:#if number is less than 0, the number is not prime (according to the Google).
        sys.exit("The number is not prime.")


# Write a program that takes a list of number and makes a new list of only the first and last elements of the given list.
# write this code inside a function.

def list_ends(a_list):
     return [a_list[0], a_list[len(a_list)-1]]


















if __name__ == "__main__":
    #    character_input()
    #    odd_or_even()
    #    list_less_than_ten()
    #    find_divisors()
    #    list_overlap()
    #    palindrome()
    # list_of_comprehensions()
    # rock_paper_scissors()
    # guess_the_number()
    # List_overlap_comprehensions()
    # primality_functions_solutions()
    list_ends()