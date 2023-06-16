import csv
from pprint import pprint


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


def get_albums():
    """
    Returns all the albums in the dataset in a list
    https://realpython.com/python-csv/
    """
    with open('albumlist.csv', encoding='latin1') as album_list:
        csv_reader = csv.reader(album_list, delimiter=',')
        for albums in csv_reader:
            return albums


get_albums()
