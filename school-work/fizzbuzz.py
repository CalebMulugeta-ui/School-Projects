s="   fly me   to   the moon  "

listWord = s.split(" ")
lastWord = ""
print(lastWord)

for i in range(len(s) -1, -1,-1):
    if listWord[i] == " ":
        continue
    else:
        lastWord = listWord
    

print(len(lastWord))

