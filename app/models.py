import random
import string
import datetime

class Connections:
    pool = {}

class UrlModel:
    
    def __init__(self):
        self.db = Connections.pool['db'].shorty
        self.coll = self.db.urls
    
    def _new_code(self):
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(6))
    
    def _new_entry(self, code, url):
        return dict(
            code = code,
            url = url,
            created_on = str(datetime.date.today())
        )
    
    def is_an_entry(self, code):
        entry = self.coll.find_one({'code':code})
        if entry:
            return True
        return False
    
    def add_entry(self, url):
        while True:
            code = self._new_code()
            if not self.is_an_entry(code):
                break
        new_entry = self._new_entry(code, url)
        e = self.coll.insert_one(new_entry)
        return self.coll.find_one({'_id':e.inserted_id})
    
    def get_entry(self, code):
        entry = self.coll.find_one({'code':code})
        return entry
