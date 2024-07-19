import sys
import pygame

# File setup for sounds
path = "/home/raspi6/lettercontainer/"
sound_files = ["0.wav", "1.wav", "2.wav", "3.wav", "4.wav", "5.wav", "6.wav", "7.wav", "8.wav", "9.wav", "A.wav", "B.wav", "C.wav", "D.wav", "E.wav", "F.wav", "G.wav", "H.wav", "I.wav", "J.wav", "K.wav", "L.wav", "M.wav", "N.wav", "O.wav", "P.wav", "Q.wav", "R.wav", "S.wav", "T.wav", "U.wav", "V.wav", "W.wav", "X.wav", "Y.wav", "Z.wav"]

# pygame setup
pygame.mixer.init(33000)
speaker_volume = 1.0 # set volume
pygame.mixer.music.set_volume(speaker_volume)

# Reading from output file
file = open('/home/raspi6/output.txt','r')
content = file.read()
print(f"Reading text:{content}")
for i in range(len(content)):
    if (content[i]) == '0':
        pygame.mixer.music.load(path + sound_files[0])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True: # to let the sound finish playing before moving to another sound file
            continue
    elif (content[i]) == '1':
        pygame.mixer.music.load(path + sound_files[1])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == '2':
        pygame.mixer.music.load(path + sound_files[2])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == '3':
        pygame.mixer.music.load(path + sound_files[3])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == '4':
        pygame.mixer.music.load(path + sound_files[4])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == '5':
        pygame.mixer.music.load(path + sound_files[5])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == '6':
        pygame.mixer.music.load(path + sound_files[6])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == '7':
        pygame.mixer.music.load(path + sound_files[7])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == '8':
        pygame.mixer.music.load(path + sound_files[8])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == '9':
        pygame.mixer.music.load(path + sound_files[9])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'a' or (content[i]) == 'A':
        pygame.mixer.music.load(path + sound_files[10])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'b' or (content[i]) == 'B':
        pygame.mixer.music.load(path + sound_files[11])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'c' or (content[i]) == 'C':
        pygame.mixer.music.load(path + sound_files[12])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'd' or (content[i]) == 'D':
        pygame.mixer.music.load(path + sound_files[13])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'e' or (content[i]) == 'E':
        pygame.mixer.music.load(path + sound_files[14])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'f' or (content[i]) == 'F':
        pygame.mixer.music.load(path + sound_files[15])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'g' or (content[i]) == 'G':
        pygame.mixer.music.load(path + sound_files[16])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'h' or (content[i]) == 'H':
        pygame.mixer.music.load(path + sound_files[17])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'i' or (content[i]) == 'I':
        pygame.mixer.music.load(path + sound_files[18])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'j' or (content[i]) == 'J':
        pygame.mixer.music.load(path + sound_files[19])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'k' or (content[i]) == 'K':
        pygame.mixer.music.load(path + sound_files[20])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'l' or (content[i]) == 'L':
        pygame.mixer.music.load(path + sound_files[21])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'm' or (content[i]) == 'M':
        pygame.mixer.music.load(path + sound_files[22])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'n' or (content[i]) == 'N':
        pygame.mixer.music.load(path + sound_files[23])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'o' or (content[i]) == 'O':
        pygame.mixer.music.load(path + sound_files[24])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'p' or (content[i]) == 'P':
        pygame.mixer.music.load(path + sound_files[25])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'q' or (content[i]) == 'Q':
        pygame.mixer.music.load(path + sound_files[26])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'r' or (content[i]) == 'R':
        pygame.mixer.music.load(path + sound_files[27])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 's' or (content[i]) == 'S':
        pygame.mixer.music.load(path + sound_files[28])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 't' or (content[i]) == 'T':
        pygame.mixer.music.load(path + sound_files[29])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'u' or (content[i]) == 'U':
        pygame.mixer.music.load(path + sound_files[30])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'v' or (content[i]) == 'V':
        pygame.mixer.music.load(path + sound_files[31])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'w' or (content[i]) == 'W':
        pygame.mixer.music.load(path + sound_files[32])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'x' or (content[i]) == 'X':
        pygame.mixer.music.load(path + sound_files[33])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'y' or (content[i]) == 'Y':
        pygame.mixer.music.load(path + sound_files[34])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    elif (content[i]) == 'z' or (content[i]) == 'Z':
        pygame.mixer.music.load(path + sound_files[35])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue

# close file
file.close()
pygame.display.quit()
pygame.quit()
sys.exit()
