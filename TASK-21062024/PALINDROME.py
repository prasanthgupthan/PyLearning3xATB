def is_palindrome(s):

    s = s.replace(" ", "").lower()

    return s == s[::-1]


test_strings = ["naman", "nitin", "level", "pramod"]

for string in test_strings:
    print(f"{string}: {is_palindrome(string)}")
