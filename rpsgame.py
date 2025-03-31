'''import random
options=['rock','paper','scissor']

play=True
while play:
    computer=random.choice(options)
    player=None
    while player not in options:
        player=input('Enter your choice [rock,paper,scissor] : ')
    if player==computer:
        print('It is a Tie..')
    elif player=='rock' and computer=='paper':
        print('You Win!')
    elif player=='papaer' and computer=='scissor':
        print('You Win!')
    elif player=='scissor' and computer=='rock':
        print('You Win!')
    else:
        print('You Lose....')
    if not input('you want to play agian!?(y/n): ').lower() == 'y':
        play=False
else:
    print('Thanks for playing ')'''

