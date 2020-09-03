def RemoveDupliChar(Word):
    NewWord = " "
    index = 0
    for char in Word:
        if char != NewWord[index]:
            NewWord += char
            index += 1
    print(NewWord.strip())


RemoveDupliChar('mississippi')
