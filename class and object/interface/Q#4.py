# Create an interface Printable with a method print. Implement this interface in classes Document, Photo, and Label with specific implementations of the print method.
 
from abc import ABC, abstractmethod
class Printable:
    @abstractmethod
    def print(self):
        pass

class Document(Printable):
    title = ''
    def __init__(self,title) :
        self.title = title

    def print(self):
        print("the title of this document is ",self.title)
class Photo(Printable):
    pixel = ''
    def __init__(self,pixel):
        self.pixel = pixel

    def print(self):
        print("this photo pixel is :",self.pixel)


class Label(Printable):
    text = ''
    def __init__(self,text):
        print("printing text",self.text)


document = Document("doc1")
photo = Photo("10px")
label = Label("hello  world")


document.print()
photo.print()
label.print()
