from random import randint
from random import shuffle
from fireman import Fireman

class Comissioner:
    """The Comissioner provides functionallity for choosing watchwords from the database and assigning them colors for gameplay.
    """
    def __init__(self):
        """constructs a new instance of Comissioner
        """
        self.watchword_ids = {}
        self.watchwords = []
        self.color_word_key = {}
    
    def generate_watchwords(self, collections, fireman):
        """generates 25 watchwords for the game. It trys to get at least one from each collection and make no duplicates
        These are stored in the member list: watchwords. 
        Also, assigns color values to the watchwords. These are stored in the member dictionary: color_word_key.

        Args:
            collections (list): the collections from which to pull watchwords
            fireman (Fireman): the Fireman object
        """
        self.color_word_key = {}
        self.watchwords = [] # reset watchwords
        results = []
        self._decide_words(collections, fireman)
        for i in collections:
            for j in self.watchword_ids[i]:
                data = fireman.get_data(i, j)
                while data in results:
                    data = fireman.get_data(i, self._get_new_word_id(i, fireman))
                results.append(data)
        shuffle(results)
        self.watchwords = results
        self._generate_color_word_key()
        self.watchword_ids = {} # reset watchword_ids for future use

    def _decide_words(self, collections, fireman):
        """gets 25 watchwords IDs for the game. It trys to get at least one from each collection
        These are stored in the member dictionary: watchword_ids.

        Args:
            collections (list): the collections from which to pull watchwords
            fireman (Fireman): the Fireman object
        """
        qtys = []
        for i in collections:
            qtys.append(fireman.get_data(i, "info", key="qty"))
            self.watchword_ids[i] = []
        is_giving_each_collection_a_chance = True
        collection_counter_index = 0
        for _ in range(25):
            if collection_counter_index > len(collections)-1:
                is_giving_each_collection_a_chance = False
            if is_giving_each_collection_a_chance:
                collection_index = collection_counter_index
                document_id = randint(1, int(qtys[collection_index]))
                self.watchword_ids[collections[collection_index]].append(str(document_id))
                collection_counter_index += 1
            else:
                is_trying = True
                while is_trying:
                    collection_index = randint(0, len(collections)-1)
                    document_id = str(randint(1, int(qtys[collection_index])))
                    if not document_id in self.watchword_ids[collections[collection_index]]: #if it is not already in the watchword_ids dict
                        self.watchword_ids[collections[collection_index]].append(str(document_id))
                        is_trying = False
                    else:
                        is_trying = True
        
    def _get_new_word_id(self, collection, fireman):
        """gets a new watchword ID that is not already in the member list: watchword_ids[collection]

        Args:
            collection (str): the collection from which to get a new watchword ID
            fireman (Fireman): the Fireman object

        Returns:
            str: new watchword ID that is not already in the member list: watchword_ids[collection]
        """
        is_trying = True
        while is_trying:
            current_list = self.watchword_ids[collection]
            qty = fireman.get_data(collection, "info", key="qty")
            document_id = str(randint(1, int(qty)))
            if not document_id in current_list: #if it is not already in the watchword_ids dict
                return document_id
            else:
                is_trying = True
    
    def _generate_color_word_key(self):
        """assigns a color to each of the words. Also, decides who starts. There will be 8 reds, 8 blues, 7 yellows, 1 black, 
        and a extra red or blue according to who starts.
        """
        words = list(self.watchwords)
        starting_player_code = randint(1,2)
        if starting_player_code == 1:
            starting_player = "red"
            self.color_word_key[words.pop()] = "red"
            for _ in range(8):
                self.color_word_key[words.pop()] = "red"
            for _ in range(8):
                self.color_word_key[words.pop()] = "blue"
        else:
            starting_player = "blue"
            self.color_word_key[words.pop()] = "blue"
            for _ in range(8):
                self.color_word_key[words.pop()] = "blue"
            for _ in range(8):
                self.color_word_key[words.pop()] = "red"
        
        self.color_word_key[words.pop()] = "black"

        for _ in range(7):
            self.color_word_key[words.pop()] = "yellow"

        shuffle(self.watchwords) # shuffle at the end

            