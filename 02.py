'''palindrome checker'''
def palindrome():
    a = input(":")
    l = a.lower()
    f = a[::-1]
    g=l[::-1]
    if l == g:
        print('This is a palindrome')
    else:
        print('This is not a palindrome')
        print(f"Its palindrome is - {g}")

palindrome()