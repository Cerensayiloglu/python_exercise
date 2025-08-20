#this this project takes the word and count vowels from wordand and shows number of vowel at turkish language
def countvowel(word):
    letter="aeuüıioöAEUÜOÖİI"
    return sum( 1 for harf in word if harf in letter)
word=input("kelimeyi girin")
print(f"bu kelimede {countvowel(word)} sesli harf var")