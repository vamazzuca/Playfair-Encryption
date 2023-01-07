# The following function will initiate the playfair cipher program.
def main():
    output_list = []
    num = input()
    for i in range(int(num)):
        keyword_string = input()
        key_list = keyword_error_check(keyword_string)
        if type(key_list) != list:
            output_list.append("ERROR")
        else:
            output_list.append(play_fair(key_list))
    for ch in output_list:
        print("\n", ch, sep = "")
            
# The following function will check to see if the user has input a keyword with
# a message.
def keyword_error_check(keyword_string):
    key_list = keyword_string.split(" ")
    if len(key_list) == 2:
        return key_list 
    return False

# The following function will encrypt a message using a playfair cypher.
def play_fair(key_list):
    table = playfair_table(key_list[0])
    encryption = playfair_encryption(table, key_list[1])
    return encryption


def playfair_table(key):
    key = remove_and_replace_x(key)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWYZ"
    key += alphabet
    key = remove_duplicates(key)
    # Following code taken from "Hints" in Assignment 1 specifications
    row_table = [key[i:i+5] for i in range(0, len(key), 5)]
    #-----------------------------------------------------
    column_table = []
    count = 0
    for num in range(0, len(key), 5):
        column = ""
        for nums in range(count, len(key), 5):
            column += key[nums]
        count += 1
        column_table.append(column)
    return (row_table, column_table)


def remove_duplicates(key):
    new_key = ""
    for ch in key:
        if ch not in new_key:
            new_key += ch
    return new_key

def remove_and_replace_x(key):
    no_x_key = ""
    for ch in key:
        if ch == "X":
            no_x_key += "KS"
        else:
            no_x_key += ch
    return no_x_key

def playfair_encryption(table, message):
    encryption_string = ""
    message = messageCheck(message)
    for i in range(0, len(message), 2):
        pair = message[i: i + 2]
        encrypt_pair = sameList(table[0], pair)
        if len(encrypt_pair) != 2:
            encrypt_pair = sameList(table[1], pair)
        if len(encrypt_pair) != 2:
            encrypt_pair = differentList(table[0], pair)
        encryption_string += encrypt_pair
    return encryption_string

def messageCheck(message):
    newMessage = ""
    for i in range(0, len(message), 2):
        pair = message[i: i + 2]
        newMessage += pair
        if len(pair) == 2:
            if pair[0] == pair[1]:
                newMessage += "Q"
    if len(newMessage) % 2 != 0:
        newMessage += "Z"
    return newMessage
                 
def sameList(table, pair):
    encrypt_pair = ""
    for row in table:
        if (pair[0] in row) and (pair[1] in row):
            if (row.find(pair[0]) + 1) == 5:
                encrypt_pair += row[0]
            else:
                encrypt_pair += row[row.find(pair[0]) + 1]
            if (row.find(pair[1]) + 1) == 5:
                encrypt_pair += row[0]
            else:
                encrypt_pair += row[row.find(pair[1]) + 1]
    return encrypt_pair

def differentList(table, pair):
    for row in table:
        if pair[0] in row:
            firstPos = table.index(row), row.find(pair[0])
        if pair[1] in row:
            secondPos = table.index(row), row.find(pair[1])
    encryptedLetterOne = table[firstPos[0]][secondPos[1]]
    encryptedLetterTwo = table[secondPos[0]][firstPos[1]]
    encrypted_pair = encryptedLetterOne + encryptedLetterTwo
    return encrypted_pair
   
       
main()
