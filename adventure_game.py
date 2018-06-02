print('Welcome to the Zoo!!! I would like to invite you to go on an amazing journey.')
print('To have more fun you may take one friend with you')
name = input('Tell me, what is your name? ')
friend = input('Great! And what is the name of your friend? ')
print('\n')
print('Awesome! Now we are ready to start!!')
print('Turn on your imagination and be ready to have fun!')
print('\n')
print('We are in the beginning  of our joorney and need to decide where to start')
print('\n')
print('''We can start with:\n '
       1 - Adventure Landing\n
       2 - African Savanna\n
       3 -  Flamingo Plaza''')
print('\n')

choice1 = int(input('Please chose where you want to start and type the number: '))
print('\n')
if choice1 <= 3 and choice1 > 0:   print('Great choice!'.upper() )
print('\n')

if choice1 == 1:
    print('{} and {}, Welcome to Adventure Landing. We have many rides that are tons of fun!'.format(name, friend))
    print('\n')
    print('Want to be a pilot? Well you\'ll need training to earn your wings - ' + 'Bush Pilot Training!'.upper())
    print('Do you want to ride the tiger? The ostrich? Or maybe the elephant? Then ' + 'Conservation Carousel'.upper() + 'is your choice!')
    print('Do you like race cars? Well, what are you waiting for? ' + 'Retro'.upper() + ' is in style with our race cars!')
    print('\n')
    print ('''It\'s time to make your choice! What do you want to do next? \n
           1 - Bush Pilot Training; \n
           2 - Conservation Carousel; \n
           3 - Retro Racing South Africa''')
    choice2 = int(input('>'))
    if choice2 == 1:
        print('Soar high, take in the view, and enjoy your flight!')
    elif choice2 == 2:
        print('Enjoy a leisurely ride with some amazing animals!')
    elif choice2 == 3:
        print('Enjoy the ride!')
    else:
    	print('I don\'t understand that command. Please start again and read the directions over.')

elif choice1 == 2:
    print('Welcome to African Savanna!!!')
    print('Here you’ll find an enormous four-acre area enclosure for our amazing elephants,')
    print('a spacious tree-filled enclosure for our lions, an aviary filled with beautiful birds, and a quiet home for our zebras.')
    print('\n')
    print('{} and {}, you may also do some activities here. '.format(name, friend ))
    print('1 - Outback Express Adventure Train.')
    print('2 - Tiger track. This ride will thrill kids and adults alike.')
    print('So, your choice!')
    choice2 = int(input('>'))
    if choice2 == 1:
        print('{} and {}, just sit back, relax, and enjoy a tour of African Savanna, featuring zebras and amazing elephants.'.format(name, friend))
    elif choice2 == 2:
        print('Awesome, this is my favourite! Loads of twists,turns and all around fun; this kiddie coaster will give you a roaring good time. Hang onto your tail!')
    else:
    	print('I don\'t understand that command. Please start again and read the directions over.')

elif choice1 == 3:
    print('{} and {}, meet our fabulous flamingos and spoonbills!'.format(name, friend))
    print('Press 1 to learn more about Lesser Flamingo, and 2 - about African Spoonbill')
    choice2 = int(input('>'))
    if choice2 == 1:
        print('''There are six species that make up the family Phoenicopteridae: greater flamingo, lesser flamingo, Chilean flamingo, Andean flamingo,
        James flamingo and American flamingo. The lesser flamingo is the smallest of the species.''')
        print('All six species of flamingo are recognized by their long legs, pink plumage and long flexible necks.')
    elif choice2 == 2:
        print('''The African spoonbill\'s long legs and thin, pointed toes help it walk easily
        through the varying depths of water and mud in search of prey.They are recognized by their long spatulate bills,
        bare red face and legs, and white plumage. The bill is bluish grey with a fringe of red along the edge of the bill.''')
    else:
    	print('I don\'t understand that command. Please start again and read the directions over.')

else:
    print('I don\'t understand that command. Please start again and read the directions over.')
