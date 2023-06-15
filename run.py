import csv
from pprint import pprint

ALBUMS = 'albumlist.csv'
all_albums = []


class Album:
    def __init__(self, number, year, album, artist, genre, subgenre):
        """
        Represents an album
        """
        self.number = number
        self.year = year
        self.album = album
        self.artist = artist
        self.genre = genre
        self.subgenre = subgenre
