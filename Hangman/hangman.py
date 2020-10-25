import random

print('H A N G M A N')
play = ''
# print('The game will be available soon.')
while True:
    play = input('\nType "play" to play the game, "exit" to quit: ')
    while play != 'play' and play != 'exit':
        play = input('Type "play" to play the game, "exit" to quit: ')
    if play != 'play':
        break
    rand_idx = random.randint(0, 3)
    attempts = 8
    won = False
    guessed_letters = []
    word_list = ['python', 'java', 'kotlin', 'javascript']
    chosen_word = word_list[rand_idx]
    hint = '-' * len(chosen_word)

    while attempts:
        appeared = False
        print('\n' + hint)
        inp = input("Input a letter: ")
        if inp in guessed_letters:
            print("You already typed this letter")
        elif len(inp) != 1:
            print('You should input a single letter')
        elif not inp.islower():
            print('It is not an ASCII lowercase letter')
        else:
            guessed_letters.append(inp)
            for j in range(len(chosen_word)):
                if inp == chosen_word[j]:
                    hint = hint[:j] + inp + hint[j + 1:]
                    appeared = True

            if not appeared:
                print("No such letter in the word")
                attempts -= 1
        if hint == chosen_word:
            won = True

    if won:
        if attempts==0:
            print('You survived!')
            print("User survived but have 8 wrong guesses. He should be hanged")
        else:
            print('You survived!')
            print('\n' + chosen_word)
            print("You guessed the word!")

    else:
        print('You lost!')
