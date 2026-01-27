import random
choices = ['rock','paper','scissor']
t_count =0
w_count = 0
g_count = 0
i_count = 0 
is_true = True
while is_true:
    user = input('Enter Your choices \n\t Your choices are [Rock,Paper,Scissor] : ').lower()
    computer = random.choice(choices)
    g_count += 1
    while user not in choices:
        
        user = input('Invalid Choice! \n\t Please enter a valid choice \n\t Your choices are [Rock,Paper,Scissor] : ')
        i_count += 1
        g_count += 1
        continue
    
    if user == computer:
        print('It is Tie')
        t_count += 1
    elif user == 'rock' and computer == 'scissor':
        print('You win the game ')
        w_count += 1
    elif user == 'paper' and computer == 'rock':
        print('You win the game')
        w_count += 1
    elif user == 'scissor' and computer == 'paper':
        print('you win the game')
        w_count += 1
    else:
        print('You loose the game')
    is_valid = True
    while is_valid:
        
        u_input = input('Do you want to play again ! (Y/N) : ').lower()
        while u_input != 'n' and u_input != 'y':
            
            u_input = input('Ivalid Choice ! \n\t Please Enter a valid choice \n\t Your choices are (Y/N) : ')
            is_valid = True
            continue
        else:
            if u_input == 'n':
                
                is_true = False
                break
            elif u_input == 'y':
                is_true = True
                break
            

print('Thank You for playing with me')
print('Total games you have played ',g_count)
print('Win score ',w_count)
print('Loose score ',g_count-w_count-t_count-i_count)
print('Tie Score ',t_count)
print('Invalid Choices ',i_count)