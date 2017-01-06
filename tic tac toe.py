import random
import time
print('''  a b c
1 _|_|_
2 _|_|_
3  | | ''')
time.sleep(2)
print('''instruction:
your move:a1

result:
 X|_|_
 _|_|_
  | |

valid moves:
a1,a2,a3,
b1,b2,b3,
c1,c2,c3.''')

valid_moves=[]
valid_moves=['a1','a2','a3','b1','b2','b3','c1','c2','c3']
time.sleep(2)
print('\n\n\n')


move=input("your move: ")
while move not in valid_moves:
    print('''not a valid move,\nvalid moves:
    a1,a2,a3,
    b1,b2,b3,
    c1,c2,c3.''')
    time.sleep(1)
    move=input("your move: ")

if move=='a1':
    print('''X|_|_
_|_|_
 | | ''')
elif move=='a2':
    print('''_|_|_
X|_|_
 | | ''')
elif move=='a3':
    print('''_|_|_
_|_|_
X| | ''')
elif move=='b1':
    print('''_|X|_
_|_|_
 | | ''')
elif move=='b2':
    print('''_|_|_
_|X|_
 | | ''')
elif move=='b3':
    print('''_|_|_
_|_|_
 |X| ''')
elif move=='c1':
    print('''_|_|X
_|_|_
 | | ''')
elif move=='c2':
    print('''_|_|_
_|_|X
 | | ''')
elif move=='c3':
    print('''_|_|_
_|_|_
 | |X''')

#this doesn't include the previous move yet
valid_moves.remove(move)
random_limit=len(valid_moves)
computer_rand = random.randint(0,random_limit)
computer_move=valid_moves[computer_rand]

time.sleep(1)
print('')
print(computer_move)

if computer_move=='a1':
    print('''O|_|_
_|_|_
 | | ''')
elif computer_move=='a2':
    print('''_|_|_
O|_|_
 | | ''')
elif computer_move=='a3':
    print('''_|_|_
_|_|_
O| | ''')
elif computer_move=='b1':
    print('''_|O|_
_|_|_
 | | ''')
elif computer_move=='b2':
    print('''_|_|_
_|O|_
 | | ''')
elif computer_move=='b3':
    print('''_|_|_
_|_|_
 |O| ''')
elif computer_move=='c1':
    print('''_|_|O
_|_|_
 | | ''')
elif computer_move=='c2':
    print('''_|_|_
_|_|O
 | | ''')
elif computer_move=='c3':
    print('''_|_|_
_|_|_
 | |O''')




