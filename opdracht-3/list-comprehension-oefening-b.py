from timeit import timeit

'''With the following code i want to show that using comprehension is going to give us easier
and undestendable aplication of what a for does. Also we can sea that an comprehension can run
than using for loops'''

code_1 = """
names = ['Ana', 'Maria', 'Gustavo','Ferrero', 'Enriaue', 'Americo', 'Marco']

names_by_m = [n for n in names if (n[0] == 'M')]
"""

code_2 = """
names = ['Ana', 'Maria', 'Gustavo','Ferrero', 'Enriaue', 'Americo', 'Marco']

names_by_m = []

for n in names:
    if(n[0] == 'M'):
        names_by_m.append(n)
"""

print('Excecution time of code with comprehension: ', timeit(code_1, number = 10_000))
print('Excecution time of code with for loop: ', timeit(code_2, number = 10_000))