import random

words = []

def make_list():
    with open('words.txt', 'r') as f:
        for line in f:
            words.extend(line.strip().split())
    #print(words)

def display_word(secret, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in secret])

def win(secret):
    print(f"\ncongratulations! you've guessed the word: {secret}")

def five():
  print("")
  print(f"|-----|")
  print(f"|    ")
  print(f"|    ")
  print(f"|    ")
  print(f"|    ")
  print("")

def four():
  print("")
  print(f"|-----|")
  print(f"|     o")
  print(f"|     ")
  print(f"|     ")
  print(f"|     ")
  print("")


def three():
  print("")
  backslash = "\\"
  print(f"|-----|")
  print(f"|     o")
  print(f"|    \\|")
  print(f"|     |")
  print(f"|     ")
  print("")

def two():
  print("")
  backslash = "\\"
  print(f"|-----|")
  print(f"|     o")
  print(f"|    \\|/")
  print(f"|     |")
  print(f"|    ")
  print("")

def one():
  print("")
  backslash = "\\"
  print(f"|-----|")
  print(f"|     o")
  print(f"|    \\|/")
  print(f"|     |")
  print(f"|    /")
  print("")

def deadman():
  print("")
  backslash = "\\"
  print(f"|-----|")
  print(f"|     o")
  print(f"|    \\|/")
  print(f"|     |")
  print(f"|    / {backslash}")
  print("")



make_list()


secret = random.choice(words).lower()
#print(secret)
guessed_letters = set()
correct_letters = set(secret)
attempts = 5


print("***hangman yay***!")
five()

while attempts > 0:
    print(f"\n{display_word(secret, guessed_letters)}\n")
    print(f"guessed letters: {', '.join(sorted(guessed_letters))}")
    print(f"remaining attempts: {attempts}")

    guess = input("\nguess a letter: ").lower()

    if guess == secret:
        win(secret)
        break

    if not guess.isalpha():
        print("\nplease enter letters.")
        continue

    if guess != secret and len(guess) != 1:
      print("\ncheating is not nice")

    if len(guess) == 1 and guess in guessed_letters:
        print("\nyou have already guessed that letter. Try again.")
        continue

    if len(guess) == 1 and guess not in guessed_letters:
        guessed_letters.add(guess)

    if guess in correct_letters:
        print("good guess!")
        if correct_letters.issubset(guessed_letters):
            win(secret)
            break
    else:
        attempts -= 1

    
    if attempts == 5:
      five()
    elif attempts == 4:
      four()
    elif attempts == 3:
      three()
    elif attempts == 2:
      two()
    elif attempts == 1:
      one()
      

if attempts == 0:
    deadman()
    print(f"\nsorry, you've run out of attempts. the word was: {secret}")
