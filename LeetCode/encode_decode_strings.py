from typing import List
# thought process, you could just havea special character to separate the words, but what if it appeared in the word itself 
# and how would you know the length of this number 
# therefore it should be a number followed by a secret character
# this is easy to encode as shown below just create a new string appending the word with the encoded key 
# then decoding is to identify this key character followed by an integer
# then slice from the start plus the length of the word (this required googling to find out how to do this)
# append this the decoded array 
# increment i by the length to move onto the next word
# else increment by 1 to move onto to the next word 

def encode(strs: List[str]) -> str:
    encoded_string = ""
    for word in strs: 
        encoded_string += f"{len(word)}#{word}"

    return encoded_string

def decode(s: str) -> List[str]:
    i = 0
    decoded_string_arr = []
    
    while i < len(s): 
        if s[i] == "#" and s[i - 1].isdigit():
            length = int(s[i - 1])
            start_of_word = i + 1
            decoded_string_arr.append(s[start_of_word: start_of_word + length])
            i += length
        i += 1
    return decoded_string_arr

def checker(og_input: List[str], given_output: List[str]) -> bool: 
    return og_input == given_output

def decodev2(s: str) -> List[str]:
    i = 0
    decoded_string_arr = []

    while i < len(s): 
        if s[i] == "#" and s[i - 1].isdigit():
            j = i - 1
            while j >= 0 and s[j].isdigit(): 
                j -= 1

            word_length = int(s[j + 1:i])
            start_of_word = i + 1
            word = s[start_of_word:start_of_word + word_length]
            decoded_string_arr.append(word)
            i += word_length
        
        i += 1
    
    print(decoded_string_arr)
    return decoded_string_arr


input1 = ["neetssssssssssssssssssssssssss","3#code","love","you"]
input2 = ["we","say",":","yes"]

encoded_string = encode(input2)
decoded_string_arr = decodev2(encoded_string)

print(checker(input2, decoded_string_arr))




