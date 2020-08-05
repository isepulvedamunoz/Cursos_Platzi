my_dict = {
    'David':35,
    'Erika':32,
    'Jaime':25,
}

print(my_dict['David'])
print(my_dict.get('Ignacio', 30))
my_dict['Ignacio'] = 31
print(my_dict)

def llaves(dict):
    for valor in dict.values():
        print(valor)

llaves(my_dict)