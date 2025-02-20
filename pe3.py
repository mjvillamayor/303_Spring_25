import string
def encode(input_text, shift):
    alphabet = list(string.ascii_lowercase)  
    shifted_text = ''
    for char in input_text:
        if char in alphabet:  
            new_index = (alphabet.index(char) + shift) % 26  
            shifted_text += alphabet[new_index]
        else:
            shifted_text += char  
    return (alphabet, shifted_text)
print(encode("xyz", 3))  # Output (['a', 'b', ..., 'z'], 'abc')
print(encode("j!K,2?", 3))  # Output  (['a', 'b', ..., 'z'], 'm!n,2?') 
