def count_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"
    s = s.replace(" ", "")  # Remove spaces for counting
    vowel_count = 0
    consonant_count = 0

    for char in s:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

# Example usage
test_string = "hello world"
vowels, consonants = count_vowels_and_consonants(test_string)
print(f"Vowels: {vowels}, Consonants: {consonants}")
