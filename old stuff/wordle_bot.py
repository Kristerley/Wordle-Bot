import json
with open("words.txt") as file:
    words_list = file.read().split('\n')
#
letters = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

count = 0

for word in words_list:
    for char in set(list(word)):
        letters[char]+=1
        count+=1

letters = dict(sorted(letters.items(), key=lambda item: item[1], reverse = True))
print(count)
json = json.dumps(letters)

with open('letters_2.json','w') as file:
    file.write(json)


# guesses = {}
# for word in words_list:
#     chars = set(list(word))
#     guesses[word] = 0
#     for char in chars:
#         guesses[word] += letters[char]
#
# guesses = dict(sorted(guesses.items(), key=lambda item: item[1], reverse = True))
# json = json.dumps(guesses)
#
# with open('guesses.json','w') as file:
#     file.write(json)
#
def wordle():
    with open('letters.json') as file: 
        letters = json.load(file)
    with open('words.json') as file: 
        words = json.load(file)
    with open('guesses.json') as file: 
        guesses = json.load(file)

    wrong_letters = set()
    correct_letters = {}
    correct_position = {}
    possible_guesses = words
    tes = ''
    for i in range(6):
        guess = max(possible_guesses,key=possible_guesses.get)
        print(guess)
        wrong_letters.update(list(input("Enter the letters that are wrong: ")))
        while True:
            corr_lett, position = (input("Enter the letter and position of correct letters"))
            if not position.isdigit():
                break
            correct_position[int(position)] = corr_lett
            tes = input("done?")
            print(correct_position)
            if tes == 'y':
                break
        while True:
            corr_lett, position = (input("Enter the letter and position of incorrect letters"))
            
            if not position.isdigit():
                break
            correct_letters[int(position)] = corr_lett
            tes = input("done?")
            print(correct_letters)
            if tes == 'y':
                break

        # correct_position.update(list(input("enter the correct letter positions -1: ")))
           
        for i in wrong_letters:
            possible_guesses = {word:value for word,value in possible_guesses.items() if i not in word}
        for i,w in correct_letters.items():
            possible_guesses = {word:value for word,value in possible_guesses.items() if w in word and word[i] != w}
        for i,w in correct_position.items():
            possible_guesses = {word:value for word,value in possible_guesses.items() if word[i] == w}

# wordle()

