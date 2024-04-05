import os

os.system("clear")

def main():
    os.system("clear")
    action = input("Do you want to convert to or from binary?\n")
    if action == "to":
        convert()
    elif action == "from":
        unconvert()
    else:
        print("Please enter a valid response")
        main()

def convert():
    string = input("Please enter your text:\n")
    binary = ''.join(format(i, '08b') for i in bytearray(string, encoding ='utf-8'))
    print()
    print("Your binary is:")
    print(binary)

def unconvert():
    binary = input("Please enter your binary:\n")
    #binary = int(binary, 2)
    string = " "
    
    # conversion
    #for i in range(0, len(binary), 7):
    #    temp_data = binary[i:i + 7]
    #    decimal_data = BinaryToDecimal(temp_data)
    #    string = string + chr(decimal_data)
    
    string = string.join(chr(int(binary[i*8:i*8+8],2)) for i in range(len(binary)//8))


    print("Your text is:")
    print(string)


main()