import time, sys, os

# color snippet
red = "\033[31m"
white = "\033[37m"
black = "\033[30m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"


#process sign
ask = f"{red}[{cyan}?{red}]{white}"
warning = f"{red}[{cyan}!{red}]{white}"
success = f"{red}[{cyan}+{red}]{white}"

ascii = (f"""
   {red}__                 __                                             
  / /_ ____   ____   / /_____   _____ ____ _ ___   _____ ____ _ _____
 / __// __ \ / __ \ / // ___/  / ___// __ `// _ \ / ___// __ `// ___/
/ /_ / /_/ // /_/ // /(__  )  / /__ / /_/ //  __/(__  )/ /_/ // /    
\__/ \____/ \____//_//____/   \___/ \__,_/ \___//____/ \__,_//_/{white}
                                    
                                  {cyan}[{white} Created by {red}putr444 {cyan}]{white}
                                                                     
""")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print(f"\n {red}[{cyan}1{red}]{white} Encrypt Plain Text\n"
          f" {red}[{cyan}2{red}]{white} Decrypt Cipher Text\n"
          f" {red}[{cyan}3{red}]{white} Exit\n"
          "\n")
    
def ascii_art():
    print(ascii)
    

# Main Program
while True:
    ascii_art()
    menu()
    while True:
        try:
            choice = int((input(f" {ask} Select one of the options > ")))
            if choice > 3 or choice <= 0:
                raise Exception
            break
        except ValueError:
            print(f" {warning} Valid Input !")
        except Exception:
            print(f" {warning} Choose In range 1-3")

    if choice == 1:
        clear_screen()
        ascii_art()
        plainText = str(input(f" {ask} Encrypt > ")).upper()
        letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        for key in range(1, len(letter)):
            encrypt = ''
            for symbol in plainText:
                if symbol in letter:
                    num = letter.find(symbol)
                    num += key

                    if num >= len(letter):
                        num -= len(letter)
            
                    encrypt += letter[num]
                else:
                    encrypt += symbol
            print(f" {success} Key [{cyan}{key}{white}] : {encrypt}")
            time.sleep(0.2)
        print(f" {success} Finished !")
        input("\n Press Enter to continue...")
        clear_screen()
        continue
                  
    elif choice == 2:
        clear_screen()
        ascii_art()
        cipherText = str(input(f" {ask} Decrypt > ")).upper()
        letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        for key in range(1, len(letter)):
            translated = ''
            for symbol in cipherText:
                if symbol in letter:
                    num = letter.find(symbol)
                    num -= key

                    if num < 0:
                        num += len(letter)

                    translated += letter[num]
                else:
                    translated += symbol
            print(f" {success} Key [{cyan}{key}{white}]: {translated}")
            time.sleep(0.2)
        print(f" {success} Finished !")
        input("\n Press Enter to continue...")
        clear_screen()
        continue
    
    elif choice == 3:
        break
