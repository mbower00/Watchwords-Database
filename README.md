# Overview

This program uses a Firestore Database to store and recieve words for a word game. Run the main.py to start the program. At start, you can either play the game, work with the database.

My purpose in writing this software was to give me digital access to one one of my favorite games: Codenames ([Rules](https://czechgames.com/files/rules/codenames-rules-en.pdf)). I also hope to use some of this code and the database to create a web app of the game. Also, I wrote this program to develop my skills, espcially in working with Cloud Databases.

[Watchwords Database Demo](https://youtu.be/ALYIkUMC280) 

[Watchwords Database: Insert, Modify, Delete, Retrieve](https://youtu.be/foSk5KsDVNE)

NOTE: these video do not show the full functionallity of the software

# Cloud Database

I am using a Firestore Database from Google. It is named Watchwords.

Watchwords is structured to hold different categories of words (collections). In each collection, there is a seperate document (named a unique number) for each word (or multi-word, for example: a country name consisting of multiple words). Each document contains a Key-Value pair of "word" : {word}. An exception is the document called "info" (each collection has one) which contains a Key-Value pair of "qty" : {number of word-documents}.\
- Category
    - "1"
        - "word" : {word}
    - "2"
        - "word" : {word}
    - n
        - "word" : {word}
    - info
        - "qty" : {number of word-documents}=
- ...


# Development Environment

I used Visual Studio Code (code editor). I also used Google Firebase (online) and Google Cloud (online). and Replit (online code editor) was also uesd for some practice and information on Cloud Database work.

I used the python language with a number or libraries.

Libraries:
- firebase_admin
    - for working with the database
- ssl
    - for sending email
- smtplib
    - for sending email
- random
    - for random numbers and suffling

# Useful Websites

* [codingem](https://www.codingem.com/python-u-in-front-of-a-string/)
* [w3schools](https://www.w3schools.com/python/python_ref_dictionary.asp)
* [w3schools](https://www.w3schools.com/python/python_ref_list.asp)
* [stackvidhya](https://www.stackvidhya.com/check-if-key-exists-in-dictionary-python/)
* [github](https://github.com/Gullesnuffs/Codenames/blob/master/wordlist-eng.txt)
* [github](https://gist.github.com/dariusz-wozniak/656f2f9070b4205c5009716f05c94067)
* [presidentsusa](https://www.presidentsusa.net/listofpresidents.pdf)
* [w3schools](https://www.w3schools.com/python/)
* [geeksforgeeks](https://www.geeksforgeeks.org/pad-or-fill-a-string-by-a-variable-in-python-using-f-string/)
* [lihaoyi](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html)
* [realpython](https://realpython.com/python-send-email/)
* [youtube](https://www.youtube.com/watch?v=v_hR4K4auoQ)
* [youtube](https://www.youtube.com/watch?v=Ofux_4c94FI&list=PLl-K7zZEsYLluG5MCVEzXAQ7ACZBCuZgZ&index=2)
* [youtube](https://www.youtube.com/watch?v=o7d5Zeic63s&list=PLl-K7zZEsYLluG5MCVEzXAQ7ACZBCuZgZ&index=4)
* [youtube](https://www.youtube.com/watch?v=haMOUb3KVSo&list=PLl-K7zZEsYLluG5MCVEzXAQ7ACZBCuZgZ&index=5)
* [firebase](https://firebase.google.com/docs/firestore/)
* [replit](https://replit.com/@cmacbeth)

# Future Work

* I could possibly try to make some of the Fireman.delete_document_and_shift() method take less time
* Use it to connect to a web app
* I could make the emails that it sends out look a bit nicer
