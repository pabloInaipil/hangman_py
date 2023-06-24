import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words) #la pc elige aleatoriamente alguna palabra del listado "word"
    while '-' in word or ' ' in words:
        word = random.choice(words)

    return word.upper()



def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letras en la palabra
    alphabet = set(string.ascii_uppercase)
    user_letters = set() # lo que el jugador a adivinado

    lives = 7

    # input usuario
    while len(word_letters) > 0 and lives >0:
        #letras usadas
        # ' '.join (['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(user_letters))

        # las letras tipeadas (ie W - R D)
        word_list = [letter if letter in user_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Adivina la palabra: ', ' '.join(word_list))


        user_letter = input('Adivina la palabra: ').upper()
        if user_letter in alphabet - user_letters:
            user_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # Va quitando vidas
                print('\nEsa letra,', user_letter, 'no esta en la palabra.')

        elif user_letter in user_letters:
            print('Ya usaste ese caracter, intenta con otro par favaar.')

        else:
            print('Caracter invalido. Intenta otra vez par favarr')

     # llegas aqui cuando se te acaban las vidas
    if lives == 0:
        print(lives_visual_dict[lives])
        print('Estas muerto, sorry. La palabra era', word)
    else:
        print('wena perro! Adivinaste la palabra', word, '!!')


if __name__ == '__main__':
    hangman()







