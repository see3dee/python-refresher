# iterate through the list of words and find words that have 'ab or ba'

passwords = ['ccavfb', 'baaded', 'bbaa', 'aaeed', 'vbb', 'aadeba', 'aba', 'dee', 'dade', 'abc', 'aae', 'dded', 'abb', 'aaf', 'ffaec']

for word in passwords:
    if 'ab' in word and 'ba' in word:
        print(f"{word} has BOTH 'ab' and 'ba' in it ")
        print('')
    elif 'ab' in word or 'ba' in word:
        print(f"{word}  has 'ab' or 'ba' in it ")
        print('')
    elif 'ab' not in word or 'ba' not in word:
        print(f"{word} has nether 'ab' nor 'ba' in it ")
        print('')
    else:
        print('all done')


for word in passwords:
    if 'a' not in word and word.startswith('v'):
        print(word)

up_low = "MissISSiPPi"

print(f"This is applying the .capitalize method for strings: ")
print(up_low.capitalize())

print(f"This is applying the .lower method for strings: ")
print(up_low.lower())

print(f"This is applying the .upper method for strings: ")
print(up_low.upper())

print(f"This is applying the .isupper method for strings: ")
print(up_low.isupper())

print(f"This is applying the .startswith method for strings: ")
print(up_low.startswith('v'))
