
def string_apart():
    str = 'jsKsOdjDbvERsS'
    str_lowers = ''
    str_uppers = ''
    for i in str:
        if i.islower():
            str_lowers += i
        else: 
            str_uppers += i

    str_lowers += str_uppers

    return str_lowers

print(string_apart(str))
    