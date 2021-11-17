if __name__ == '__main__':
     s= 'jathin'
     print(len(s))
     # First character is index 0
     print(s[1:5])
     # print first 3 letters
     print(s[:3])
     # print last 3 letters
     print(s[-3:])
     # print last 3 letters from an offset
     print(s[-3:-1])
     print(s.count('a')) # count of a
     print(s.index('a')) # index of a - first instance
     print(s.rindex('a')) # rindex of a - reverse first instance

     #Printing tabs and newlines
     s1='ab\nefg\tgh\txy\bm' # \b is backspace
     print(s1)
     print('*******************')
     s2 = 'ab\\n\nefg\tgh'
     print(s2)

     #Unicode or UTF - Python uses Unicode (Larger code set somethign similar to ASCII for conversion and byte level storage'

     print("I can't")
     print('I can\'t') #printing using single quotes
     print("Hello Jathin")
     print('Hello Jathin')
     print('Hello "\'Jathin\'"')

