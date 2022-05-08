from email_file import email_file
from fireman import Fireman
from comissioner import Comissioner
from librarian import Librarian
from spokesman import Spokesman

def main():
    """the main fuction.
    Instantiates the Fireman, Spokesman, Comissioner, and Librarian objects.
    Allows the user to choose between playing the game, working with the database, and ending the program.
    """
    fireman = Fireman()
    librarian = Librarian()
    comissioner = Comissioner()
    spokesman = Spokesman(comissioner)

    user_choice = ""
    while user_choice != "done":
        print("\nWelcome to Watchwords!")
        print("[1] Play")
        print("[2] Manage Database")
        print("['done'] Finish")
        user_choice = input("> ")
        if user_choice == "1":
            play_game(fireman, comissioner, spokesman)
        elif user_choice == "2":
            manage_database(fireman, librarian)

def manage_database(fireman, librarian):
    """allows the user work with the database.

    Args:
        fireman (Fireman): the Fireman object
        librarian (Librarian): the Librarian object
    """
    is_making_first_choice = True
    while is_making_first_choice:
        is_making_second_choice = False
        print("\nWatchwords Database:")
        print("[1] Insert")
        print("[2] Modify")
        print("[3] Delete")
        print("[4] Retrieve")
        user_choice = input("('done' to finish) > ")
        if user_choice == "1" or user_choice == "2" or user_choice == "3" or user_choice == "4":
            is_making_second_choice = True
        elif user_choice == "done":
            is_making_first_choice = False

        if is_making_second_choice:
            if user_choice == "1": # Insert
                print("Insert:")
                print("[1] Word")
                print("[2] Whole File")
                user_choice = input("> ")
                if user_choice == "1":
                    print("Insert:")
                    collection = input("Please enter a collection > ")
                    value = input("Please enter a value > ")
                    fireman.set_data(collection, value)
                elif user_choice == "2":
                    print("Insert:")
                    collection = input("Please enter a collection > ")
                    value = input("Please enter a file > ")
                    print("This may take a moment...")
                    librarian.transcribe(collection, value, fireman)
            elif user_choice == "2": # Modify
                print("Modify:")
                print("[1] Replace")
                print("[2] Add To")
                user_choice = input("> ")
                print("Modify:")
                collection = input("Please enter a collection > ")
                print("Modify:")
                document = input("Please enter a word ID > ")
                if user_choice == "1":
                    value = input("Please enter a value > ")
                    fireman.set_data(collection, value, document=document)
                elif user_choice == "2":
                    value = input("Please enter a value > ")
                    fireman.add_to_data(collection, document, value)
            elif user_choice == "3": # Delete
                print("Delete:")
                print("[1] Word")
                print("[2] Whole Collection")
                user_choice = input("> ")
                collection = input("Please enter a collection > ")
                if user_choice == "1":
                    document = input("Please enter a word ID > ")
                    print("This may take a moment...")
                    fireman.delete_document_and_shift(collection, document)
                elif user_choice == "2":
                    fireman.delete_collection(collection)
            elif user_choice == "4": # Retrieve
                print("Retrieve:")
                collection = input("Please enter a collection > ")
                print("Retrieve:")
                document = input("Please enter a word ID or 'all' > ")
                if document == "all":
                    print("This may take a moment...")
                    words_and_ids = fireman.get_all_words_from_collection(collection)
                    for i in words_and_ids:
                        print(f"{i}: {words_and_ids[i]}")
                else:
                    print(fireman.get_data(collection, document))

def play_game(fireman, comissioner, spokesman):
    """allows the user to play the game

    Args:
        fireman (Fireman): the Fireman object
        comissioner (Comissioner): the Comissioner object
        spokesman (Spokesman): the Spokesman object
    """
    is_playing = True
    should_email = input("Email Answer? [y] > ")
    if should_email == "y":
        sender_password = input("Please enter sender password > ")
        receiver_email_address_1 = input(f"Please enter email of codemaker #1 > ")
        receiver_email_address_2 = input(f"Please enter email of codemaker #2 > ")
    word_pack = ""
    word_packs = []
    while word_pack != "done":
        word_pack = input(f"Please enter a word pack to add ('done' to finish) {word_packs} > ")
        if word_pack != "done":
            word_packs.append(word_pack)
    while is_playing:
        comissioner.generate_watchwords(word_packs, fireman)
        answer_file = spokesman.give_answers("answers.txt")
        if should_email == "y":
            email_file(answer_file, receiver_email_address_1, sender_password)
            email_file(answer_file, receiver_email_address_2, sender_password)
        spokesman.display_board(True)
        print("Enter: [COL][ROW] ('done' to finish) ", end="")
        while True:
            result = spokesman.get_and_convert_row_col_input()
            if result == "_done_":
                break
            spokesman.color_watchword(result)
            print("\n\n\n\n\n\n\n")
            spokesman.display_board(False)
        if input("Play again? [y] > ") != "y":
            is_playing = False

if __name__ == "__main__":
    main()