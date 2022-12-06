import random
from words import words
import string

def get_vaild_word(words):
    word=random.choice(words)
    return word.upper()
def hangman():
    word=get_vaild_word(words)
    word_letters= set(word)
    alphabet=set(string.ascii_uppercase)
    used_letter=set()
    lives=6
    while len(word_letters)>0 and lives >0:
        print('Used Letters:',' '.join(used_letter))
        word_list=[letter if letter in used_letter else '_' for letter in word]
        print('Current word',''.join(word_list))
        user_letter= input('Guess a letter: ').upper()
        if user_letter in alphabet-used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives=lives-1
                print("wrong! you have", lives," chance!!")
        elif user_letter in used_letter:
            print("already used")
        else:
            print("invaild")
    if lives==0:
        print("game over")
        print("the word is ",word,"\n\n")
    else:
        print(f"you won!! the word is {word}\n\n")

hangman()
