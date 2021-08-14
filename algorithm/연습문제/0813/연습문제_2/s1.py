def itoa(my_int):
    my_str = []

    while my_int != 0:
        r = my_int % 10
        char = chr(r + ord('0'))
        my_str.append(char)
        my_int //= 10

    my_str.reverse()

    result = ''.join(my_str)

    return result

print(itoa(123)) # => '123'
print(type(itoa(123)))