alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(original_text, shift_amount):
    encrypted_message = " "
    original_text.lower()
# shift_amount data type is integer. original_text = string

    #Loop each letter in the text for shifting.
    for letter in original_text:
        l_idx = alphabet.index(letter) #Find the index of the letter in the alphabet and store it in a variable. (integer)
        l_idx += shift #Add that variable to the shift amount.
        if l_idx > 25: #conditional statement to make sure the variable is within the alphabet range
            l_idx -= 26  #You can also use a modulo operation where. l_idx %= len(alphabet) <---- Logic, It divides the l_index by 26 and the remainder becomes the variable.

        #Use the new letter index to shift and produce a new letter.
        encrypted_message += alphabet[l_idx] #Store the new letters
    print(encrypted_message)



encrypt(original_text= text,shift_amount= shift)