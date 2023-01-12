import random
words = ['hello','computer','integer','selection','movement','patterns','user'] #add words you want to be in your game to this list
word = words[random.randint(0,len(words))-1]
guesses = 11
letters_guessed = []

#print the unknown word
for i in word:
    print('_ ', end = '')
print('')

while True: #main game loop
    guess = input('Enter a guess: ').lower()
    letters_guessed.append(guess)
    
    if guess == word: #user has won
        print('Well done, you win!!')
        break
    
    correct = False
    for i in word: #print the word after you have made guesses
        if i in letters_guessed:
            print(f'{i} ',end='')

        else:
            print('_ ', end = '')
        
        if i == guess:
            correct = True
    
    #check if the user has correctly guessed all letters
    correctly_guessed_all = True
    for i in word:
        if i not in letters_guessed:
            correctly_guessed_all = False
            
    print('')
    if correctly_guessed_all: #user has won
        print('Well done, you win!!')
        print(f'The word was {word}')
        break
    
    if not correct:
        print('Oh no! That guess is incorrect! -1 guesses!')
        guesses -= 1
    else:
        print('That guess was correct!')
        
    if guesses == 0:
        print(f'You loose! Out of guesses!! Word was {word}')
        break
    
    #print the letters that the user has guessed already
    print('You have guessed: ',end='')
    for i in letters_guessed:
        print(f'{i} ',end='')
    
    #print the amount of guesses the user has less
    print('')
    print(f'You have {guesses} guesses left!')
    print('')