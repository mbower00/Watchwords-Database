from random import randint
from comissioner import Comissioner

class Spokesman:
    def __init__(self, comissioner):
        """constructs a new instance of Spokesman.
        Stores the passed Comissioner object as a member.

        Args:
            comissioner (Comissioner): The Comissioner object
        """
        self.comissioner = comissioner
        self.RED = "\u001b[31m"
        self.YELLOW = "\u001b[33m"
        self.BLUE = "\u001b[34m"
        self.BLACK = "\u001b[30m"
        self.NORMAL = "\u001b[00m"

    def display_board(self, is_first_time, target="default", cell_length_measure_wordset="default"):
        """displays the game board to the target

        Args:
            is_first_time (bool): whether this is the first time this game board with these watchword values has been displayed
            target (str, optional): The file in which to display the game board. Defaults to "default" which displays to the terminal.
            cell_length_measure_wordset (list, optional): A list from which to measure the cell length. Defaults to "default" which uses the member's member: comissioner.watchwords.
        """
        if is_first_time:
            if cell_length_measure_wordset == "default":
                self.length = self._get_largest_watchword_length(self.comissioner.watchwords) + 2
            else:
                self.length = self._get_largest_watchword_length(cell_length_measure_wordset) + 2
            self.length_in_spaces = ""
            self.length_in_dashes = ""
            for _ in range(self.length):
                self.length_in_spaces += " "
            for _ in range(self.length):
                self.length_in_dashes += "-"
        watchword_index = 0
        if target == "default":
            print(f"-{self.length_in_dashes}-{self.length_in_dashes}-{self.length_in_dashes}-{self.length_in_dashes}-{self.length_in_dashes}-")
        else:
            with open(target, "a") as the_file:
                print(f"-{self.length_in_dashes}-{self.length_in_dashes}-{self.length_in_dashes}-{self.length_in_dashes}-{self.length_in_dashes}-", file=the_file)
        for _ in range(5):
            if target == "default":
                print("|", end="")
            else:
                with open(target, "a") as the_file:
                    print("|", end="", file=the_file)
            for _ in range(5):
                word = self.comissioner.watchwords[watchword_index]
                if word.find("\u001b[") != -1:
                    spacing_length = self.length+10
                else:
                    spacing_length = self.length
                if target == "default":
                    print(f"{word : ^{spacing_length}}|", end="")
                else:
                    with open(target, "a") as the_file:
                        print(f"{word : ^{spacing_length}}|", end="", file=the_file)
                watchword_index += 1
            if target == "default":
                print(f"\n-{self.length_in_dashes}-{self.length_in_dashes}-{self.length_in_dashes}-{self.length_in_dashes}-{self.length_in_dashes}-")
            else:
                with open(target, "a") as the_file:
                    print(f"\n-{self.length_in_dashes}-{self.length_in_dashes}-{self.length_in_dashes}-{self.length_in_dashes}-{self.length_in_dashes}-", file=the_file)
    
    def give_answers(self, target="default"):
        """displays the answers (watchwords with corrisponding color) to target

        Args:
            target (str, optional): The file name used (with ".txt" at the end) to make a file in which to display the answer. The created file's name will have an ID. Defaults to "default" which displays to the terminal.

        Returns:
            str: the new file's name
        """
        original_wordset = list(self.comissioner.watchwords)
        if target != "default":
            is_adding_id = True
            while is_adding_id:
                file_id = randint(1,999)
                temp_target = target
                temp_target = temp_target.replace('.txt', f"_ID_{file_id}.txt")
                try:
                    with open(temp_target, "x"):
                        pass
                    is_adding_id = False
                except:
                    temp_target = target
            target = temp_target
            print(f"Answer File ID: {file_id}")
        if target == "default":
            for word in self.comissioner.watchwords:
                self.color_watchword(word)
            self.display_board(True, target=target, cell_length_measure_wordset=original_wordset)
            self.comissioner.watchwords = original_wordset # reset watchwords set
        length = self._get_largest_watchword_length(self.comissioner.watchwords)
        table_length = (length + 2) * 5 + 6
        color_length = 6
        for i in self.comissioner.color_word_key:
            if target == "default":
                color = self.comissioner.color_word_key[i].upper()
                to_print = f"{i :-<{length+2}}{color :->{color_length}}"
                print(f"{to_print : ^{table_length}}")
            else:
                with open(target, "a") as the_file:
                    color = self.comissioner.color_word_key[i].upper()
                    to_print = f"{i :-<{length+2}}{color :->{color_length}}"
                    print(f"{to_print}", file=the_file)
        return target

    def _get_largest_watchword_length(self, wordset):
        """gets the length of the largest string in a list of strings

        Args:
            wordset (list): the list of strings

        Returns:
            int: the length of the largest string in wordset
        """
        largest_len = 0
        for i in wordset:
            length = len(i)
            if largest_len < length:
                largest_len = length
        return largest_len

    def color_watchword(self, word):
        """adds the correct color code to the passed word in the watchwords list of the commisioner

        Args:
            word (str): the word to color
        """
        color = self.comissioner.color_word_key[word]
        index = self.comissioner.watchwords.index(word)

        if color == "red":
            colored_word = self.RED + word + self.NORMAL
        elif color == "blue":
            colored_word = self.BLUE + word + self.NORMAL
        elif color == "yellow":
            colored_word = self.YELLOW + word + self.NORMAL
        elif color == "black":
            colored_word = self.BLACK + word + self.NORMAL

        self.comissioner.watchwords[index] = colored_word

    def uncolor_watchword(self, word):
        """adds the normal color code to the passed word in the watchwords list of the commisioner

        Args:
            word (str): the word to uncolor
        """
        index = self.comissioner.watchwords.index(word)

        if word.find(self.RED) != -1:
            word.replace(self.RED, self.NORMAL)
        elif word.find(self.BLUE) != -1:
            word.replace(self.BLUE, self.NORMAL)
        elif word.find(self.BLACK) != -1:
            word.replace(self.BLACK, self.NORMAL)
        elif word.find(self.YELLOW) != -1:
            word.replace(self.YELLOW, self.NORMAL)

        self.comissioner.watchwords[index] = word
    
    def get_and_convert_row_col_input(self):
        """gets input from the user ([row][column]) and returns the value located at that row and 
        column if the word has not already been guessed this game

        Returns:
            str: the word that the user guessed
        """
        is_asking = True
        while is_asking:
            user_input = input("> ")
            if user_input == "done":
                return "_done_"
            if len(user_input) == 2:
                col = int(user_input[0])
                row = int(user_input[1])
                if row in range(1,6) and col in range(1,6):
                    word = self.comissioner.watchwords[((row-1)*5)+(col-1)]
                    if word.find("\u001b[") == -1:
                        is_asking = False
        return word