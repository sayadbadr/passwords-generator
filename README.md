this is some tools for generate the passwords from a word-lists
<br>you can use the code "password.py" as a normal user
<br>  e.g: python password.py
      <br>      +Enter the path to your words file: g:\projects\words\words.txt
<br>      +Enter the password length: 8
<br>      +Choose Mode: 'custom' or 'random': random
<br>      +Choose password composition: 
<br>        1 - Words only (W)
<br>        2 - Words + Numbers (W + N)
<br>        3 - Words + Symbols (W + S)
<br>        4 - Words + Numbers + Symbols (W + N + S)
<br>        5 - Numbers only (N)
<br>        6 - Symbols only (S)
<br>        7 - Numbers + Symbols (N + S)
<br>      +Enter your choice (1-7): 4
<br>      +How many passwords to generate (e.g., 1000, 100000, 1000000): 1000
<br>      +Enter the path to save the passwords file (e.g., passwords.txt): password.txt
<br>       Generating 1000 passwords...
<br>       Passwords saved to password.txt
<br>      <br> or you use the tool "pswd.py" in the terminal in 'linux' or 'windows'
<br>  e.g: python pswd.py -w wordlist.txt -l 8 -m r -c 4 -g 1000 -o password.txt
