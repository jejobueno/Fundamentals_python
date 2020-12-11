#This si a list with 5 different objects
my_data = [1.32, 'Hola', 44, 40, 'e']
print(f'my_data : {my_data}')

#list from 0 to 1000 ussing comprehension
numbers = [ x for x in range(1001)]
print(f'"numbers" list start in {numbers[0]} and finish in {numbers[-1]}')

#Another way to make list:

#1. List of chars
sentence = list('This is a sentence that will be sotred in a char list')

#2. List of lists
lists = [my_data, numbers, sentence]

#3. An empty list
empty_list = []
