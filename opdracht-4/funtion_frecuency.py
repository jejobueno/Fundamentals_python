products = ['apple', 'cosas', 35, None, 48, 12.4, 12.4]

def frecuency(list_of_values):
    dictionary = {x: list_of_values.count(x) for x in list_of_values}
    print(dictionary)
        
frecuency(products)