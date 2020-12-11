import keyword


def constrains_keyboard(*args):
    for k in args:
        if keyword.iskeyword(k) == True:
            return True
    else:
        return False
        
print(constrains_keyboard('hello', 'goodbye'))
print(constrains_keyboard('def', 'haha', 'lol', 'chickens are evil',42))
print(constrains_keyboard('for','four','if'))
print(constrains_keyboard('blabla', 'doggo', 'crab', 'anchor'))
print(constrains_keyboard('gizzly', 'ignore', 'return', 'False',))
