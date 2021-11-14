from Day_08_art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


print(logo)


def caesar(cipher, input_text, shift_amount):
    result_text = ""
    for letter in input_text:
        if cipher == "encode" and letter in alphabet:
            new_position = alphabet.index(letter) + shift_amount
            if new_position > len(alphabet):
                new_shift_position = new_position // len(alphabet)
                new_position = new_position - (len(alphabet) * new_shift_position)
            result_text += alphabet[new_position]
        elif cipher == "decode" and letter in alphabet:
            if shift_amount > len(alphabet):
                new_shift_amount = shift_amount // len(alphabet)
                shift_amount = shift_amount - (len(alphabet) * new_shift_amount)
            new_position = alphabet.index(letter) - shift_amount
            result_text += alphabet[new_position]
        else:
            result_text += letter
    print(f"The {cipher}d text is {result_text}")


if __name__ == "__main__":

    should_end = False
    while not should_end:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(cipher=direction, input_text=text, shift_amount=shift)

        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if restart == "no":
            should_end = True
            print("Goodbye")


# вариант преподавателя
# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for char in start_text:
#     if char in alphabet:
#       position = alphabet.index(char)
#       new_position = position + shift_amount
#       end_text += alphabet[new_position]
#     else:
#       end_text += char
#   print(f"Here's the {cipher_direction}d result: {end_text}")
#
# from Day_08_art import logo
# print(logo)
#
#
# should_end = False
# while not should_end:
#
#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))
#   shift = shift % 26
#
#   caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
#
#   restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#   if restart == "no":
#     should_end = True
#     print("Goodbye")