# Design an interface Storable with a method store. Implement this interface in classes File, DatabaseRecord, and Cache with specific implementations of the store method.


from abc import ABC, abstractmethod


class Storeable:
    @abstractmethod
    def store(self):
        pass


class File(Storeable):
    file = ''

    def __init__(self, file):
        self.file = file

    def store(self):
        print("storing data in file:", self.file)


class DatabaseRecord(Storeable):
    data = ''

    def __init__(self, data):
        self.data = data

    def store(self):
        print("the record of database is :", self.data)


class Cashe(Storeable):
    data = ''

    def __init__(self, data):
        self.data = data

    def store(self):
        print("the data store in :", self.data)


file = File("python practise")
data = DatabaseRecord("server")
cashe = Cashe("database")

file.store()
data.store()
cashe.store()
