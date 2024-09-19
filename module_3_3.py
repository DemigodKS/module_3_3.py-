def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [5.66, 'apple', False]
values_dict = {'a': 1, 'b': 'строка', 'c': True}

values_list_2 = ['b', 6.755555]

#1
print_params()
print_params(c = False)
print_params(a = 4, b = 7)
print_params(b = 25)
print_params(c = [1,2,3])
#2
print_params(*values_list)
print_params(**values_dict)
print_params(values_list, values_dict)
#3
print_params(*values_list_2, 42)
