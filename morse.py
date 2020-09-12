import win32api,win32con
import win32com.client as comclt
import time

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-',' ':' '} 
  
# Function to encrypt the string 
# according to the morse code chart 
def encrypt(message): 
    cipher = '' 
    for letter in message: 
        if letter != ' ':
            # Looks up the dictionary and adds the 
            # correspponding morse code 
            # along with a space to separate 
            # morse codes for different characters 
            cipher += MORSE_CODE_DICT[letter] + ' '
        else: 
            # 1 space indicates different characters 
            # and 2 indicates different words 
            cipher += ' '
  
    return cipher 
  
# Function to decrypt the string 
# from morse to english 
def decrypt(message): 
  
    # extra space added at the end to access the 
    # last morse code 
    message += ' '
  
    decipher = '' 
    citext = '' 
    for letter in message: 
  
        # checks for space 
        if (letter != ' '): 
  
            # counter to keep track of space 
            i = 0
  
            # storing morse code of a single character 
            citext += letter 
  
        # in case of space
        else: 
            # if i = 1 that indicates a new character 
            i += 1
  
            # if i = 2 that indicates a new word 
            if i == 2 : 
  
                 # adding space to separate words 
                decipher += ' '
            else: 
  
                # accessing the keys using their values (reverse of encryption) 
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                .values()).index(citext)] 
                citext = '' 
  
    return decipher
def dot(wsh):
    wsh.SendKeys("{CAPSLOCK}")
    time.sleep(0.5)
    wsh.SendKeys("{CAPSLOCK}")
    #time.sleep(0.5)

def dash(wsh):
    wsh.SendKeys("{CAPSLOCK}")
    time.sleep(1)
    wsh.SendKeys("{CAPSLOCK}")
    #time.sleep(1.0)

def space():
    time.sleep(1.5)

def space2():
    time.sleep(2)    

def convert_to_led(result):
    wsh= comclt.Dispatch("WScript.Shell")
    lresult=list(result)

    for data in lresult:
        if(data=='.'):
            print '.'
            dot(wsh)
        elif(data=='-'):
            print '-'
            dash(wsh)
        elif data==' ':
            print ' '
            space2()
        else:
            print ' '
            space()
    
# Hard-coded driver function to run the program 
def main(): 
    message = "Hello Everyone"
    result = encrypt(message.upper())
    
    print (result) 
    #convert_to_led(result)
    #message = "--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ... "

    #result = decrypt(result) 
    #print (result) 
  
# Executes the main function 
if __name__ == '__main__': 
    main() 
