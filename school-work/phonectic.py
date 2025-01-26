def prepText():
    paragraph = input('Enter Paragraph: ').lower()

    #Remove non-alphapet
    split=list(paragraph)
    newLetters = []
    for i in split:
        convertNum = ord(i)
        if (convertNum >= 97 and convertNum <= 122) or convertNum == 32:
            newLetters.append(i)
    listWords = (''.join(newLetters)).split(' ')
    return listWords

def createDict(listWords):
    d = {}
    for i in range(97, 123):
        letter = chr(i)
        d[letter] = []
        for word in listWords:
            if word and word[0] == letter:
                d[letter].append(word)
    return d

def main():
    print(createDict(prepText()))

main()