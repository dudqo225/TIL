def atoi(my_str):
    value = 0
    i = 0

    while i < len(my_str):
        char = my_str[i]
        digit = ord(char) - ord('0')
        value = value * 10 + digit
        i += 1

    return value

print(atoi('1234')) # => 1234
print(type(atoi('1234')))