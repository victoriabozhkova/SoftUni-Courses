def palindrome_string(word):
    if word == word[::-1]:
        return word


words = input().split(" ")
palindrome = input()

palindrome_words = [word for word in words if palindrome_string(word)]

palindrome_count = palindrome_words.count(palindrome)
print(palindrome_words)
print(f"Found palindrome {palindrome_count} times")
