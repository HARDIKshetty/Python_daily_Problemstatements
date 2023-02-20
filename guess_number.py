import random

def rand_number():
    rand = random.randrange(1, 100)
    return rand
a = rand_number()
print(a)
game_over = False
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
diff = input("Choose a difficulty. Type 'easy' or 'hard': hard: ")

if diff == "easy":
    life = 5
elif diff == "hard":
    life = 10
else:
    print("Enter Valid Option")
    
    
while not game_over:
    guess = int(input("Make a guess: "))
    if life == 0:
        print("Game Over")
        game_over= True
        break
    elif guess == a:
        print(f"You got it! The answer was {a}")
        game_over= True
        break
    elif guess> a:
        print("Too High")
        game_over= False
        life = life-1
        print(life)
    elif guess<a:
        print("Too Low")
        game_over= False
        life = life-1
        print(life)