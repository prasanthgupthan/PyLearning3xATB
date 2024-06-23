def are_anagrams(s1, s2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # Check if sorted characters of both strings are the same
    return sorted(s1) == sorted(s2)

# Example usage
s1 = "silent"
s2 = "listen"
print(f"Are '{s1}' and '{s2}' anagrams? {are_anagrams(s1, s2)}")  # Output: True

# More examples
anagram_pairs = [("namo", "mano"), ("namo", "onam")]

for pair in anagram_pairs:
    print(f"Are '{pair[0]}' and '{pair[1]}' anagrams? {are_anagrams(pair[0], pair[1])}")
