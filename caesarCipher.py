# ================================================================
# caesarCipher.py
# TODO: Compare output to an English dictionary and find which keyTest is the most likely message.
# TODO: Links conversion. Forward-slash '/' correct conversion

# ================================================================
# Initial variables

import os

symbolString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz `1234567890-=~!@#$%^&*()_+?:;,.<>\/\\'
# lengthOfSymbolString = len(symbolString) # = 86

# Test Data
testMessage = 'Hello my friends!'
testKey = 70
testMode = 'e'

# ================================================================
# cipherMessage Encryption/Decryption Function
def cipherMessage(message, key, mode):

    # Growing output string
    outputString = ''

    # Convert message to symbolIndex
    for character in message:
    
        lengthSymbolString = len(symbolString)

        symbolIndex = symbolString.find(character)

        # Handle mode; encrypt or decrypt
        if mode == 'e':
            encodedIndex = symbolIndex + key
        elif mode == 'd':
            encodedIndex = symbolIndex - key

        # Create outputString
        # Wrap around when encodedIndex is greater than the length of the symbolString
        if encodedIndex > len(symbolString) - 1:
            outputString = outputString + symbolString[encodedIndex % lengthSymbolString]
        
        # Wrap around when encodedIndex is less than zero (negative)
        elif encodedIndex < 0:
            localIndex = len(symbolString) - (encodedIndex % lengthSymbolString)
            outputString = outputString + symbolString[lengthSymbolString - localIndex]
        
        # When encodedIndex within the symbolString
        else:
            outputString = outputString + symbolString[encodedIndex]
    
    print(outputString)
    return outputString

# ================================================================
# Magic Decryption

# Output location of the magicDecryption() function
desktopPath = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
# desktopPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

def magicDecryption(message):
    
    print ('messagesOutput.txt location:\n' + desktopPath)
    
    # Create/overwrite messagesOutput.txt document.
    messagesOutput = open(desktopPath + '\\messagesOutput.txt', 'w')
    messagesOutput.write('Keys:'  + '\n')
    messagesOutput.write('====================================='  + '\n')
    messagesOutput.close()

    # Loop through every key combination and write it to file.
    for keyTest in range(86):
        keyTestMessage = cipherMessage(message, keyTest, 'd')
        messagesOutput = open(desktopPath + '\\messagesOutput.txt', 'a')
        messagesOutput.write(str(keyTest) + ': '+ keyTestMessage + '\n')
        messagesOutput.close()