vowels = ["a", "e", "i", "o", "u"]


def countVowels(word):
    i = 0
    small_word  = word.lower()
    for letter in small_word:
        if letter in vowels:
          i +=1
    return i    

word = input("Insira uma palavra: ")
print(countVowels(word))
