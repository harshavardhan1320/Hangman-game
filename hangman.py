
import hangman_names
import random


print(hangman_names.welcome())

words=(hangman_names.word_list)
random_words=random.choice(words)
len=len(random_words)

blanks=[]
for blank in range(len):
    blank="_"
    blanks+=blank
print(blanks)

lives=6
end_of_game=False

while not end_of_game:
    guess=input("Guess a letter ").lower()
    for char in range(len):
        letter=random_words[char]
        if letter==guess:
            blanks[char]=letter 
    print(blanks)

    if guess not in random_words:
        lives-=1
        if lives==0:
            end_of_game=True
            print("You have loosen the game :( ")


    if "_" not in blanks:
        end_of_game=True
        print("you won ;)")
    
    print(f"lives left are {lives}")
