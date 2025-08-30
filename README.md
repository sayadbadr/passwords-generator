#password generator
these is some tools for generate the passwords from a word-lists
<br>you can use this python program "password.py" as a normal user
<br>______e.g: python password.py
<br>______+Enter the path to your words file: g:\projects\words\words.txt
<br>______+Enter the password length: 8
<br>______+Choose Mode: 'custom' or 'random': random
<br>______+Choose password composition: 
<br>________1 - Words only (W)
<br>________2 - Words + Numbers (W + N)
<br>________3 - Words + Symbols (W + S)
<br>________4 - Words + Numbers + Symbols (W + N + S)
<br>________5 - Numbers only (N)
<br>________6 - Symbols only (S)
<br>________7 - Numbers + Symbols (N + S)
<br>______+Enter your choice (1-7): 4
<br>______+How many passwords to generate (e.g., 1000, 100000, 1000000): 1000
<br>______+Enter the path to save the passwords file (e.g., passwords.txt): password.txt
<br>________Generating 1000 passwords...
<br>________Passwords saved to password.txt
<br>------------------------------------------------------------------------------------------
<br>or you can use the tool "pswd.py" in the terminal in 'linux' or 'windows'
<br>______e.g: python pswd.py -w wordlist.txt -l 8 -m r -c 4 -g 1000 -o password.txt
<br>for more information or getting help, type:
<br>______"python pswd.py -h" or "python pswd.py --help"
