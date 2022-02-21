input_string = list(input("Enter the Encoded String >> "))

for key in range(1, 26):
    decoded_string = []  
    for char in input_string:
        if char.isalpha():
            if (char.islower() and ((ord(char) + key) > 122)) or (char.isupper() and ((ord(char) + key) > 90)):
                decoded_string.append(chr(ord(char) + key - 26))
            else:
                decoded_string.append(chr(ord(char) + key))
        else:
            decoded_string.append(char)
    print(''.join(decoded_string))            


            

