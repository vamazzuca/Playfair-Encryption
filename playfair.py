#-----------------------
# Name: Vittorio Mazzuca
# Program: playfair.py
#-----------------------


# The following function will initiate the playfair cipher program.
def main():
    outputList = []
    print("Input: ")
    num = input("\n")
    for i in range(int(num)):
        keywordString = input("\n")
        keyList = keywordErrorCheck(keywordString)
        # If only a key is input "ERROR" is displayed
        if type(keyList) != list:  
            outputList.append("ERROR")
        else:
            outputList.append(playFair(keyList))
    # All error and encrypted messages are added to outputList
    print("\n", "Output: ", sep = "")
    for ch in outputList:
        print("\n", ch, sep = "")

            
# The keywordErrorCheck function will check to see if the user has input a 
# keyword with a message.
def keywordErrorCheck(keywordString):
    keyList = keywordString.split(" ")
    if len(keyList) == 2:
        return keyList 
    return False


# The playFair function will encrypt a message using the playfair cypher.
def playFair(keyList):
    tables = playFairTable(keyList[0])
    encryption = playFairEncryption(tables, keyList[1])
    return encryption


# The playFairTable function will create and return two lists: a list of the
# rows of the table and a list of the columns of the table. 
def playFairTable(key):
    key = removeAndReplaceX(key)
    key += "ABCDEFGHIJKLMNOPQRSTUVWYZ"
    key = removeDuplicates(key)
    # Following creates the row table
    rowTable = [] 
    for rowi in range(0, len(key), 5): 
        rowTable.append(key[rowi: rowi + 5])
    # Following creates the column table
    columnTable = [] 
    for columni in range(5):
        columnString = key[columni]
        for num in range(columni, 20, 5):
            columnString += key[num + 5]
        columnTable.append(columnString)
    return rowTable, columnTable


# The removeDuplicates function will remove all the duplicate letters in the key.
def removeDuplicates(key):
    newKey = ""
    for ch in key:
        if ch not in newKey:
            newKey += ch
    return newKey


# The removeAndReplaceX function will find "X" in the string and replace it with
# "KS" instead.
def removeAndReplaceX(string):
    newString = ""
    for ch in string:
        if ch == "X":
            newString += "KS"
        else:
            newString += ch
    return newString


# The playfairEncryption function will call a series of functions that will
# use the column or row table to encrypt a message based on the playfair cipher
# methods.
def playFairEncryption(tables, message):
    encryptionString = ""
    message = (False, message)
    while message[0] == False:
        message = messageCheck(message[1])
    for i in range(0, len(message[1]), 2):
        pair = message[1][i: i + 2]
        # Checks row table first
        encryptPair = sameString(tables[0], pair)
        # Then checks column table
        if len(encryptPair) != 2:
            encryptPair = sameString(tables[1], pair)
        # If the the pair is in neither then they are in different strings
        if len(encryptPair) != 2:
            encryptPair = differentString(tables[0], pair)
        encryptionString += encryptPair
    return encryptionString


# The messageCheck function loops through the message provided by the user to 
# insert a "Q" between any identical pairs and adds a "Z" to any uneven message.
def messageCheck(message):
    newMessage = ""
    message = removeAndReplaceX(message)
    for i in range(0, len(message), 2):
        pair = message[i: i + 2]
        if len(pair) == 2:
            if pair[0] == pair[1]:
                newMessage += pair[0] + "Q" + pair[1]
                return (False, newMessage + message[i + 2:])
            else:
                newMessage += pair
        else:
            newMessage += pair[0]
    if len(newMessage) % 2 != 0:
        newMessage += "Z"
    return (True , newMessage)




# The sameString function will check to see if the pair is in the same string.
# If the are in the same string then the letter next to each is added to the
# encrypted pair.
def sameString(table, pair):
    encryptPair = ""
    for row in table:
        if (pair[0] in row) and (pair[1] in row):
            # If shift exceeds the index range of the string, loop around to 0
            if (row.find(pair[0]) + 1) == 5:
                encryptPair += row[0]
            else:
                encryptPair += row[row.find(pair[0]) + 1]
            # Perform same action but for the second letter in the pair
            if (row.find(pair[1]) + 1) == 5:
                encryptPair += row[0]
            else:
                encryptPair += row[row.find(pair[1]) + 1]
    return encryptPair


# The differentString function will find the location of the two letter pairs
# and add the ecnrypted letter to a pair based on the opposing letters position.
def differentString(table, pair):
    for row in table:
        if pair[0] in row:
            firstPos = table.index(row), row.find(pair[0])
        if pair[1] in row:
            secondPos = table.index(row), row.find(pair[1])
    encryptedLetterOne = table[firstPos[0]][secondPos[1]]
    encryptedLetterTwo = table[secondPos[0]][firstPos[1]]
    encryptedPair = encryptedLetterOne + encryptedLetterTwo
    return encryptedPair
 
        
main()