from random import randint
import random

# sick_days krijgt een value tussen 1 en 10
sick_days = randint(1,11)

calling_in_sick = False

while(sick_days > 0):

    actually_sick = random.choice([True,False])


    if actually_sick == True:
        kind_sick = False
    else:
        kind_sick = True    

    dont_feel_like_like_it = random.choice([True,False])


    if actually_sick and sick_days > 0:
        calling_in_sick = True
    elif kind_sick and dont_feel_like_like_it and sick_days > 0:
        calling_in_sick = True
    else:
        calling_in_sick = False
    sick_days -= 1
    
    print(f' You have still {sick_days} sick days')
    print(f' and you are calling in sick: {calling_in_sick}')
            