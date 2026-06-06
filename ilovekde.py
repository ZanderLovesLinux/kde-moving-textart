import os
import time

#put the word you want to use here
word = "iwillgivemysoultokde"

kdelogo = [
"                                                    xxxx",
"                                           xxxxxxxxxxxxx               xxxxxxxxx",
"                                           xxxxxxxxxxxxx             xxxxxxxxxxxxxxxxx",
"                                           xxxxxxxxxxxxx            xxxxxxxxxxxxxxxxx",
"                                           xxxxxxxxxxxxx          xxxxxxxxxxxxxxxxx",
"                                           xxxxxxxxxxxxx        xxxxxxxxxxxxxxxxxx",
"                           ww              xxxxxxxxxxxxx       xxxxxxxxxxxxxxxxx",
"                         wwwwwww           xxxxxxxxxxxxx     xxxxxxxxxxxxxxxxx",
"                       wwwwwwwwwwww        xxxxxxxxxxxxx    xxxxxxxxxxxxxxxxx",
"                      wwwwwwwwwwwwwwwwwwww xxxxxxxxxxxxx  xxxxxxxxxxxxxxxxx",
"                       wwwwwwwwwwwwwwwwwww xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"                        wwwwwwwwwwwwwwwww  xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"                         wwwwwwwwwwwwww    xxxxxxxxxxxxxxxxxxxxxxxxxxx",
"                           wwwwwwwww       xxxxxxxxxxxxxxxxxxxxxxxxxxx",
"                           wwwwwww         xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"                          wwwwww           xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"                     wwwwwwwwww            xxxxxxxxxxxxx  xxxxxxxxxxxxxxxxx",
"              wwwwwwwwwwwwwwwww            xxxxxxxxxxxxx   xxxxxxxxxxxxxxxxx",
"              wwwwwwwwwwwwwwww             xxxxxxxxxxxxx     xxxxxxxxxxxxxxxxx",
"              wwwwwwwwwwwwwwww             xxxxxxxxxxxxx      xxxxxxxxxxxxxxxxx",
"              wwwwwwwwwwwwwwww             xxxxxxxxxxxxx        xxxxxxxxxxxxxxxxx",
"              wwwwwwwwwwwwwwww             xxxxxxxxxxxxx         xxxxxxxxxxxxxxxxx",
"                    wwwwwwwwwww            xxxxxxxxxxxxx           xxxxxxxxxxxxxxxxx",
"                         wwwwwww           xxxxxxxxxxxxx            xxxxxxxxxxxxxxxxx",
"                          wwwwwww          xxxxxxxxxxxxx         www  xxxxxxxxxxxxxxx",
"                           wwwwwww         xxxxxxxxx            wwwwww xxxxxxx",
"                          wwwwwwwwwww                         wwwwwwwww",
"                        wwwwwwwwwwwwwwww                   wwwwwwwwwwwwwww",
"                      wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"                      wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww wwwwwwwwwwwwww",
"                        wwwwwwwww         wwwwwwwwwwwwww         wwwwwwwwww",
"                          wwww             wwwwwwwwwwww             wwwww",
"                                           wwwwwwwwwwww",
"                                            wwwwwwwwww",
"                                            wwwwwwwwww",
"                                             wwwwwwww"]


#when frame moves it shifts all letter's position back one. Also I set it to an if and elif so you can set different colors for the k and the gear
frame = 0
def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    clearscreen()
    for row in kdelogo:
        newrow = ""
        for pos, char in enumerate(row):
            if char == "w":
                letter_index = (pos + frame) % len(word)
                newtuff = "\033[94m" + str(word[letter_index]) + "\033[0m"
                newrow = newrow + newtuff
            elif char == "x":
                letter_index = (pos + frame) % len(word)
                newtuff = "\033[37m" + str(word[letter_index]) + "\033[0m"
                newrow = newrow + newtuff
            else:
                newrow = newrow + char
        print("\033[91m" + newrow + "\033[0m")
    frame = frame + 1
    time.sleep(0.1)

