#use of random library to construct computer choice
import random

options = ['rock', 'paper', 'scissors']
prompt = """
    1. Rock 
    2. Paper 
    3. Scissors\n\n"""

#Function determines the winner through both options
def winner(computer_option, self_option):
    swin = 'You are the winner!\n'
    cwin = 'The Computer won try again :[\n'
    tie = 'You have tied with the Computer\n'
    
    #determines all tie scenarios
    if computer_option == self_option:
        return tie
    
    #Implement the rules of rock paper scissors
    if computer_option == 'rock' and  self_option == 'paper':
        return swin
    if computer_option == 'rock' and  self_option == 'scissors':
        return cwin
    if computer_option == 'paper' and  self_option == 'scissors':
        return swin
    if computer_option == 'paper' and  self_option == 'rock':
        return cwin
    if computer_option == 'scissors' and  self_option == 'rock':
        return swin
    if computer_option == 'scissors' and  self_option == 'paper':
        return cwin

def main():
    option = input('[p]lay or [q]uit: ')
    option = option.lower()
    
    #Start game loop
    while option != 'q':
        if option == 'p':
            #create computers choice through random index between 0-2
            computer_option = options[random.randrange(1,3)]
            
            #get correct user choice
            try:
                choose = int(input(prompt))
            except:
                print("\nUH OH, YOU ARE DUMB")
                continue
            if choose != 1 and choose != 2 and choose != 3:
                continue
            self_option = options[choose-1]

            print(f'\nComputer chose: {computer_option}')
            print(f'You chose: {self_option}\n')
            
            #call winner function to determine winner of the game
            print(winner(computer_option, self_option))

        option = input('[p]lay or [q]uit: ')
        option = option.lower()

    print("\nThanks for playing!")

if __name__ == "__main__":
    main()
