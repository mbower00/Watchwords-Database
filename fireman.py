# used code from https://firebase.google.com/docs/firestore/
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Fireman:
    """The Fireman is a firebase helper. He provides functionallity for
    for working with the database
    """
    def __init__(self):
        """constructs a new instance of Fireman
        """
        firebase_admin.initialize_app(credentials.Certificate('watchwords-mulch-a4eba30f5996.json'))
        self.db = firestore.client()
        self.auto_increment_log = {}
    
    def set_data(self, collection, value, document="ai", key="word"):
        """set a record to the database. 
        If document="ai", it will auto increment according to the 'qty' value stored in the 'info' document.

        Args:
            collection (string): the collection to add to
            value (_type_): the value to set
            document (string): the document to add to. Defaults to "ai".
            key (string): the key for the value. Defaults to "word".
        """
        if document == "ai":
            document = self.auto_increment(collection)
        self.db.collection(collection).document(document).set({key : value})
    
    def add_to_data(self, collection, document, value, key="word"):
        """adds the value to the selected value in the database

        Args:
            collection (string): the collection to add to
            document (string): the document to add to.
            value (_type_): the value to add
            key (str, optional): the key of the value to add to. Defaults to "word".
        """
        added_value = self.get_data(collection, document, key=key) + value
        self.set_data(collection, added_value, document=document)

    def delete_document_and_shift(self, collection, document):
        """deletes a specified document and shifts to next documents' ID back one to fill in the space (by deleting and setting).
        Also, updates the 'qty' value stored in the 'info' document

        Args:
            collection (string): the collection 
            document (string): the document 
        """
        self._delete_single_document(collection, document)
        qty = int(self.get_data(collection, document="info", key="qty"))
        if str(qty) != document:
            for i in range(int(document)+1, qty+1):
                i = str(i) 
                value = self.get_data(collection, i)
                self._delete_single_document(collection, i)
                self.set_data(collection, value, document=str(int(i)-1))
        self.set_data(collection, str(qty-1), document="info", key="qty") #update the info document

    def _delete_single_document(self, collection, document):
        """deletes a single document.
        DOES NOT SHIFT IDS

        Args:
            collection (string): the collection 
            document (string): the document 
        """
        self.db.collection(collection).document(document).delete()

    def delete_collection(self, collection):
        """deletes a collection.
        Only will work if all documents are 1 through qty (the "info" document) plus the "info" document.

        Args:
            collection (string): the collection 
        """
        qty = int(self.get_data(collection, document="info", key="qty"))
        for i in range(1, qty+1):
            i = str(i)
            self._delete_single_document(collection, i)
        self._delete_single_document(collection, "info")

    def get_data(self, collection, document, key="word"):
        """get the value at location

        Args:
            collection (str): the collection from which to get data
            document (str): the document from which to get data
            key (str, optional): the key from which to get data. Defaults to "word".

        Returns:
            _type_: the value at the key
        """
        doc = self.db.collection(collection).document(document).get()
        if doc.exists:
            return doc.to_dict()[key]

    def get_all_words_from_collection(self, collection):
        """gets all the watchwords and their IDs from a collection

        Args:
            collection (str): the collection from which to get data

        Returns:
            dict{ID: watchword (NOTE: may be multiple words in one string)}: A dictionarry with all the watchwords and their IDs from a collection
        """
        result = {}
        qty = int(self.get_data(collection, document="info", key="qty"))
        for i in range(1, qty+1):
            result[str(i)] = self.get_data(collection, str(i))
        return result

    def auto_increment(self, collection):
        """gets an auto incremented value according to the passed collection

        Args:
            collection (string): the current collection

        Returns:
            int: an auto incremented number according to the current selection
        """
        doc = self.db.collection(collection).document("info").get()
        if doc.exists:
            new_value = str(int(self.get_data(collection, "info", key="qty")) + 1)
            self.set_data(collection, new_value, document="info", key="qty")
        else:
            new_value = "1"
            self.set_data(collection, new_value, document="info", key="qty")
        return new_value