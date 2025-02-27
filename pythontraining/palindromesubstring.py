def is_palindrome(s):
    return s == s[::-1]

def find_palindrome_substrings(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):  
            substring = s[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return list(palindromes)

def is_palindrome_input(value):
    value = str(value).replace("  "," ").lower()
    return is_palindrome(value)

def main():
    while True:
        value = input("Enter a number or string or 'exit' to quit: ")
        if value.lower() == 'exit':
            print("Exiting out of the loop.")
            break
        if is_palindrome_input(value):
            print(f"'{value}' is a palindrome.")
        else:
            print(f"'{value}' is not a palindrome.")
        
        palindromes = find_palindrome_substrings(value)
        if palindromes:
            print("Palindrome substrings found:", palindromes)
        else:
            print("No palindrome substrings found.")
        
main()
