def start_with_vowel_sound(text):
    vowel_sounds = ["xr", "yt", "a", "e", "i", "o", "u"]
    for vowel in vowel_sounds:
        if text.find(vowel) == 0:
            return True

def extract_consonant(text):
    vowels = ["a", "e", "i", "o", "u", "y"]
    consonant = ""
    for letter in text:
        if (letter not in vowels) or (letter=="u" and consonant[-1] == "q") or (letter == "y" and consonant==""):
            consonant += letter
        else:
            break
    return consonant, text.replace(consonant, '')

def translate_word (text):
    if start_with_vowel_sound(text):
        return text + "ay"
    consonant, rest = extract_consonant(text)
    return rest + consonant + "ay"

def translate(text):
    words = text.split()
    return " ".join([translate_word(word) for word in words])
