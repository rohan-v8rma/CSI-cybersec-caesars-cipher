encoded_string = list(input("Enter the Encoded String >> "))

for key in range(1, 26):
    decoded_string = []  
    for char in encoded_string:
        if char.isalpha():
            error_correction = 0 
            # this variable ensures that if Z is incremented by 1 position, we end up with A 
            # and not the ASCII character corresponding with 91
            if (char.islower() and ((ord(char) + key) > 122)) or (char.isupper() and ((ord(char) + key) > 90)):
                error_correction = 26
            decoded_string.append(chr(ord(char) + key - error_correction))
        else:
            decoded_string.append(char)
    print(''.join(decoded_string))            


            

