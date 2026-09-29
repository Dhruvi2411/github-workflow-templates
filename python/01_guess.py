from random import shuffle

def shuffle_list(l1):
    shuffle(l1)
    return l1

def input_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input("Enter number 0, 1, 2: ")
    
    return int(guess)

a = ['', '0', '']

shuffle_list(a)
guess = input_guess()

print("Winner..!!" if a[guess] == '0' else "Try again..!!")
