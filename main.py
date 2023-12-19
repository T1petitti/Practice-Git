# This is a sample Python script.
def multiply_two_nums(intA, intB):
    product = intA * intB
    print(f'The product of {intA} and {intB} is {product}\n')

def access_elements_from_list():
    c_list = ['sally', 45, ['bunny', [ 9, 'data'], None], False, None, 'Bob']
    int1 = c_list[1] #45
    int2 = c_list[2][1][0] #9
    print(f'{int1} is at index 1 and {int2} is at index 0 of index 1 of index 2\n')

sample_dict = {
    'name': 'Alice',
    'age' : 30,
    'height' : 5.5,
    'is_registered' : False
}

def format_dict(dict_param):
#    for key, value in dict_param.items():
#        print(f'{key} --> {value}\n')
    for key in dict_param:
        print(f'{key} --> {dict_param[key]}')
    print('\n')

def check_string_is_valid_num(string_param):
    try:
        float(string_param)
        return True
    except ValueError or TypeError:
        return False

if __name__ == '__main__':
    multiply_two_nums(2, 8)
    access_elements_from_list()
    format_dict(sample_dict)
    print(check_string_is_valid_num(12))
    print(check_string_is_valid_num("420.69"))
    print(check_string_is_valid_num("apple"))
    print(check_string_is_valid_num(True))

    print("Testing from TestBranch committing to Github")

