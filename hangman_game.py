import random
import hangman_stages
import Word_File
#word_list=["apple","beautiful","potato"]
lives=6
chosen_word=random.choice (Word_File.Words)
print (chosen_word)
display=[]
for i in range(len(chosen_word)): #0 1 2 3 4 5
    display +='_'
print(display)
game_over=False
while not game_over:
    guessed_letter=input("guess a letter:").lower() #p _ p p _ _
    for position in range(len(chosen_word)): #0 1 2 3 4
        letter = chosen_word[position]
        if letter==guessed_letter:
            display[position]= guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives ==0:
            game_over = True
            print("you lose!!")
    if '_' not in display:
        game_over=True
        print("You win!!")
    print(hangman_stages.stages[lives])