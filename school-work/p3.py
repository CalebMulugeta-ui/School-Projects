
#Input for user to put in their paragraph
userParagraph = input("Please write a paragraph and hit eneter when you're finished:")

#split the user input into words by spaces
words = userParagraph.split()
#Count the number of words in the user input
wordCount = len(words)

#Split the user input into sentences using period ('.') 
sentences = userParagraph.split('.')
#Get the number of sentences
sentenceCount = len(sentences)
#Subtract 1 from the sentence count to account for the extra split
properCount = sentenceCount - 1 

#Print number of words and number of sentences
print(f"Total number of words = {wordCount}")
print(f"Total Number of sentences = {properCount}")
print("Capitalized sentences are: ")

#Capitilize the first letter of each sentence using for loops/strip
for eachSentence in sentences:
   hello = eachSentence.strip()
   if hello:
      print(hello[0].upper() + hello[1:])
      
   
    
    