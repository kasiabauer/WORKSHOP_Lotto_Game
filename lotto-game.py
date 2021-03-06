from random import shuffle
'''A console game for Lotto. Where user choose 6 numbers in range 1-49 and a computer
randomly pick 6 number in the same range. Player wins if 3 hits are made.'''

num_list = []
print('Pick 6 numbers from range 1-49.')
i = 1
while len(num_list) < 6:
    try:
        num = int(input(f'Choose {i} number: '))
        if num > 49:
            raise Warning
        i += 1
        num_list.append(num)
        num_list.sort()
    except ValueError:
        print('Numbers only.')
    except Warning:
        print('Pick a number from range 1-49:')

print(f'Your numbers: {num_list}')


num_lotto = list(range(1, 50))
shuffle(num_lotto)
lotto_result = num_lotto[0:6]
lotto_result.sort()
print(f'Lotto numbers: {lotto_result}')


hits = 0
for user_num in num_list:
    if user_num in lotto_result:
        hits += 1
print(f'You have {hits} hits')

if hits >= 3:
    print(f'You win a prize for {hits} hits')
else:
    print('You loose - not enough hits.')
