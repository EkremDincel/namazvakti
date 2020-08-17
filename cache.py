import pickle

class Cache():

    def __init__(self, file_name):
        self.d = {}
        self.file_name = file_name
        try:
            self.load()
        except (FileNotFoundError, EOFError):
            self.save()

    def get(self, item):
        return self.d.get(item)

    def __getitem__(self, item):
        return self.d[item]
    
    def __setitem__(self, item, value):
        self.d[item] = value
        self.save()
        
    def load(self):
        with open(self.file_name, "rb") as f:
            self.d = pickle.load(f)

    def save(self):
        with open(self.file_name, "wb") as f:
            pickle.dump(self.d, f)

    def __repr__(self):
        return repr(self.d)
    
