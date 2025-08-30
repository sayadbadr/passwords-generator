# password generator
these is some tools for generate the passwords from a word-lists
<br>you can use this python program "password.py" as a normal user
'''
e.g: python password.py
+Enter the path to your words file: g:\projects\words\words.txt
+Enter the password length: 8
+Choose Mode: 'custom' or 'random': random
+Choose password composition: 
1 - Words only (W)
2 - Words + Numbers (W + N)
3 - Words + Symbols (W + S)
4 - Words + Numbers + Symbols (W + N + S)
5 - Numbers only (N)
6 - Symbols only (S)
7 - Numbers + Symbols (N + S)
+Enter your choice (1-7): 4
+How many passwords to generate (e.g., 1000, 100000, 1000000): 1000
+Enter the path to save the passwords file (e.g., passwords.txt): password.txt
Generating 1000 passwords...
Passwords saved to password.txt
'''
<br>or you can use the tool "pswd.py" in the terminal in 'linux' or 'windows'
<br>______e.g: python pswd.py -w wordlist.txt -l 8 -m r -c 4 -g 1000 -o password.txt
<br>for more information or getting help, type:
<br>______"python pswd.py -h" or "python pswd.py --help"
