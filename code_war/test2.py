def get_count(sentence):

    sentence = sentence.lower()
    
    count_vowel = 0
    vowels = ('a', 'e', 'i', 'o', 'u',)
    
    for letter in sentence:
        if letter in vowels:
            count_vowel += 1
    return count_vowel
        
print(get_count('joaovictoragrella'))