#this project first take text from user after that split words from text and finally shows words
text=input("metni girin")
words=text.split()
for i in range(len(words)):
    print(words[i])