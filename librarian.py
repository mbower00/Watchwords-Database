from fireman import Fireman

class Librarian:
    """The Librarian is a text file helper. She provides functionallity for reading 
    text files and transcribing them to the database (with the help of the Fireman object)
    """
    def __init__(self):
        """constructs a new instance of Librarian
        """
        self.library = {}
    
    def read(self, filename, ignore="#", store=True):
        """reads a file and stores or returns the lines (in capitalized form)

        Args:
            filename (str): the file's name
            ignore (str, optional): A character that, when on a line in the file, will cause the line to be ignored. Defaults to "#".
            store (bool, optional): Whether to store (True) in the member "library" under key <filename>, or return (False) the list of lines. Defaults to True.

        Returns:
            list: the lines of the file. ONLY RETURNS IF store IS False.
        """
        result = []
        with open(filename, "r") as text_file:
            for i in text_file:
                if i.find(ignore) == -1: # if there is no <ignore> on the line...
                    result.append(self._capitalize_multi_word(i.strip()))
        if store == False:
            return result
        else:
            self.library[filename] = result
    
    def transcribe(self, collection, filename, fireman):
        """adds data for a file from the member "library" to a database. 
        If the data for the file is not yet in the member "library", 
        it will call the read() method to add it. 

        Args:
            collection (str): the db collection to add to
            filename (str): the file's name 
            fireman (Fireman): the Fireman object for the database
        """
        if not filename in self.library:
            self.read(filename)
        for i in self.library[filename]:
            fireman.set_data(collection, i)
    
    def _capitalize_multi_word(self, word):
        """capitalizes each word in a string, even if the string has with multple words

        Args:
            word (str): the string with 1 to n words

        Returns:
            str: string with each word in a string capitalized (even if the string has with multple words).
        """
        if word.find(" ") == -1:
            return word.capitalize()
        else:
            capitalized_multi_word = ""
            words = word.split(" ")
            for i in words:
                capitalized_multi_word += i.capitalize()
                capitalized_multi_word += " "
            return capitalized_multi_word.strip()