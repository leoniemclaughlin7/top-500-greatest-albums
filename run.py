import csv
from pprint import pprint
from tabulate import tabulate


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
        # next(album_list)
        all_albums = []
        for albums in csv_reader:
            all_albums.append(albums)
        return all_albums


def print_albums(album_data):
    """
    Prints all albums to screen minus subgenre and genre
    https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
    https://learnpython.com/blog/print-table-in-python/
    """
    trimmed_albums = []
    for i in album_data:
        album_list_trimed = i[:4]
        trimmed_albums.append(album_list_trimed)
    print(tabulate(trimmed_albums, headers='firstrow', tablefmt='fancy_grid'))


def menu():
    """
    Prints user menu to screen
    """
    print("Please choose a selection from the menu below:")
    print("1 - Show all albums")
    print("2 - Show owned albums")
    print("3 - search albums")
    get_user_choice()


def get_user_choice():
    """
    Takes user input and directes user to their chossen selection
    """
    while True:
        user_choice = input('Please choose an option from the list above:\n')
        if user_choice == str(1):
            print_albums(all_albums)
        elif user_choice == str(2):
            print("option 2 - owned")
        elif user_choice == str(3):
            print("option 4 - search")
        else:
            print("Invalid input, please choose again!")
            continue


all_albums = get_albums()
menu()
