import random
options=['rock','paper','scissor']
win_count=0
lose_count=0
no_of_games=0
play=True
while play:
    computer=random.choice(options)
    player=None
    player=input('Enter your choice [rock,paper,scissor] : ')
    while player not in options:
        print('Invalid choice, please try again.')
        player=input('Enter your choice [rock,paper,scissor] : ')
    no_of_games += 1
    if player==computer:
        
        print('It is a Tie..')
    elif player=='rock' and computer=='paper':
        win_count+=1
        print('You Win!')
    elif player=='paper' and computer=='scissor':
        win_count+=1
        print('You Win!')
    elif player=='scissor' and computer=='rock':
        win_count+=1
        print('You Win!')
    else:
        lose_count+=1
        print('You Lose....')
    if not input('you want to play agian!?(y/n): ').lower() == 'y':
        play=False
else:
    ties = no_of_games - win_count - lose_count
    print('Game Over!')
    print('Thanks for playing ')
    print('Your Score:')
    print('Wins:', win_count)
    print('Losses:', lose_count)
    print('Ties:', ties)
    print('Total Games:', win_count + lose_count + ties)
