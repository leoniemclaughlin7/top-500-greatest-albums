import csv
from pprint import pprint
from tabulate import tabulate

owned_albums = None


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
    print("2 - Show owned list")
    print("3 - Search albums")
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
            print_owned(owned_albums)
        elif user_choice == str(3):
            print("option 4 - search")
        else:
            print("Invalid input, please choose again!")
            continue


def get_owned(album_data):
    """
    gets album from list based on user input and returns album
    and artist in string format. 
    https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
    """
    album_ranking = input("Please input the ranking of the album you would like to add:\n") 
    selected_album = album_data[int(album_ranking)]
    owned_album = []
    owned_album.append(selected_album[2])
    owned_album.append(selected_album[3])
    result = "Album:{} Artist:{}".format(*owned_album)
    return result


def add_albums_owned(owned_album):
    """
    adds album to list of owned albums
    """
    owned_albums.append(owned_album)
    return owned_albums


def print_owned(owned_albums):
    """
    Prints to screen users owned albums
    """
    if owned_albums is None:
        print("You have not added anything to this list yet!")
    else:
        print(*owned_albums)


def owned_menu():
    """
    displayes to the user if tehy would like to add album 
    or return to main menu.
    """



all_albums = get_albums()
menu()
owned_album = get_owned(all_albums)
owned_albums = add_albums_owned(owned_album)

