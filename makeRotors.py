import pickle
import random

# alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# rotors
def makeRotor () :
    return ''.join(random.sample(alphabet,len(alphabet)))

w1 = makeRotor()
w2 = makeRotor()
w3 = makeRotor()

handle = open('rotor.machine', 'ab')
pickle.dump((w1,w2,w3), handle)
handle.close()