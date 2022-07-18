import pickle

# alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# read rotor
handle = open('rotor.machine', 'rb')
rotor1,rotor2,rotor3 = pickle.load(handle)
handle.close()

# reflector
def reflector(char):
    return alphabet[-(alphabet.find(char)+1)] 


def encodeOneChar(char):
    char1 = rotor1[alphabet.find(char)] 
    char2 = rotor2[alphabet.find(char1)]
    char3 = rotor3[alphabet.find(char2)]
    reflected = reflector(char3)
    char3 = alphabet[rotor3.find(reflected)] 
    char2 = alphabet[rotor2.find(char3)]
    char1 = alphabet[rotor1.find(char2)]
    return char1


# rotate rotors
def rotateRotors():
    global rotor1, rotor2, rotor3
    rotor1 = rotor1[1:] + rotor1[0]
    if state % 26 :
        rotor2 = rotor2[1:] + rotor2[0]        
    if state % (26*26) :
        rotor3 = rotor3[1:] + rotor3[0]


# start working
word = 'moho'
code = ''
state = 0

for char in word:
    state += 1
    code += encodeOneChar(char)
    rotateRotors()

print(code)