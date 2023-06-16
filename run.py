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
        all_albums = []
        for albums in csv_reader:
            all_albums.append(albums)
        return all_albums


def print_albums(data):
    """
    Prints all albums to screen minus subgenre
    https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
    """
    for i in data:
        album_list_trimed = i[:4]
        print(*album_list_trimed)


all_albums = get_albums()
print_albums(all_albums)
