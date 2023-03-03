from art import logo
print(logo)
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def caesar(text,shift,direction):
        if direction=='encode':
            encrypt_text=""
            for letter in text:
                if letter in alphabet:
                    pos=alphabet.index(letter)
                    new_pos=pos+shift
                    encrypt_text+=alphabet[new_pos]
                else:
                    encrypt_text+=letter
            print(f"The encrypted text is {encrypt_text} ")
        elif direction=='decode':
            decrypt_text=""
            for letter in text:
                if letter in alphabet:
                    pos=alphabet.index(letter)
                    new_pos=pos-shift
                    decrypt_text+=alphabet[new_pos]
                else:
                    decrypt_text+=letter
            print(f"The decrypted text is {decrypt_text} ")
should_continue=True
while(should_continue):
    direction=input("Type encode to encrypt text and decode to decrypt text: ").lower()
    text=input("Enter the text: ").lower()
    shift=int(input("Enter the shift value: "))
    shift=shift%26
    caesar(text,shift,direction)
    result=input("Type yes if you wish to continue,otherwise type no: ")
    if result=="no":
        should_continue=False
        print("Good Bye!")
        
