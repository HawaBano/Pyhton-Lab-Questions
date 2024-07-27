# Create an interface Playable with a method play. Implement this interface in classes Song, Video, and Game with specific implementations of the play method.

from abc import ABC, abstractmethod


class Playable(ABC):
    @abstractmethod
    def play(self):
        pass


class Song(Playable):
    title = ''
    artist = ''

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def play(self):
        print("this sing is singing by :", self.artist)


class Vedio(Playable):
    title = ''
    director = ''

    def __init__(self, title, director):
        self.title = title
        self.director = director

    def play(self):
        print("the vedio director is :", self.director)


class Game(Playable):
    title = ''
    developer = ''

    def __init__(self, title, developer):
        self.title = title
        self.developer = developer

    def play(self):
        print("this game iis develope by :", self.developer)


song = Song("songtitle1", "artist1")
vedio = Vedio("vedio1", "director1")
game = Game("game1", "developer1")

song.play()
vedio.play()
game.play()
