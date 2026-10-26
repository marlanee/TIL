def password(s, shift):

    result = ''

    for char in s:
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')
            new_index = (index - shift) % 26
            result += chr(new_index + ord('A'))
        else:
            result += char

    return result

print(password('KHOOR', 3))