from art import logo
from replit import clear
import re

clear()
print(logo)

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','_','-','+','=','|','{','}','[',']',':',';',',','.']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"\nHere's the {cipher_direction}d result: {end_text}\n")

continue_caesar = True
while continue_caesar:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if re.match("encode",direction) or re.match("decode",direction):
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    end_caesar = input("Type 'yes' to continue otherwise type 'no'\n").lower()
    if end_caesar == "no":
      continue_caesar = False
      print("Good Bye.\n")
  else:
    print("Please choose a valid option.\n")
