import csv
from pprint import pprint
from tabulate import tabulate
import search


owned_albums = []


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
        next(album_list)
        all_albums = []
        for albums in csv_reader:
            all_albums.append(albums)
        return all_albums


def print_albums(album_data):
    """
    Prints all albums to screen minus subgenre and genre
    https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
    https://learnpython.com/blog/print-table-in-python/
    https://pypi.org/project/tabulate/
    """
    trimmed_albums = []
    for i in album_data:
        album_list_trimed = i[:4]
        trimmed_albums.append(album_list_trimed)
    max_widths = [None, None, 35, 15]
    print(tabulate(trimmed_albums,
          headers=["Ranking", "Year", "Album", "Artist"],
          tablefmt='grid', maxcolwidths=max_widths))


def menu():
    """
    Prints user menu to screen
    """
    print("Please choose a selection from the menu below:")
    print("1 - Show all albums")
    print("2 - Show top 100 albums")
    print("3 - Show owned list")
    print("4 - Search albums")
    get_user_choice()


def get_user_choice():
    """
    Takes user input and directes user to their chossen selection
    """
    while True:
        user_choice = input('Please choose an option from the list above:\n')
        if user_choice == str(1):
            print_albums(all_albums)
            owned_menu()
        elif user_choice == str(2):
            print_top_100(all_albums)  
        elif user_choice == str(3):
            print_owned(owned_albums)
        elif user_choice == str(4):
            search_menu()
        else:
            print("Invalid input, please choose again!")
            continue


def get_owned(album_data):
    """
    gets album from list based on user input and returns album
    and artist in string format, then appends to new list owned_albums
    https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
    """
    album_ranking = input("Please input the ranking of the album you would \
                           like to add:\n")
    selected_album = album_data[int(album_ranking)]
    owned_album = []
    owned_album.append(selected_album[2])
    owned_album.append(selected_album[3])
    result = "Album:{} Artist:{}\n".format(*owned_album)
    owned_albums.append(result)
    menu()
    return owned_albums


def print_owned(owned_albums):
    """
    Prints to screen users owned albums
    https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
    """
    if not owned_albums:
        print("You have not added anything to this list yet!")
        owned_menu()
    else:
        print(*owned_albums)
        owned_menu()


def owned_menu():
    """
    displayes a menu to user to add album to owned list
    """
    print("1 - Add album to owned list")
    print("2 - Return to main menu")
    user_choice = input('Please choose an option from the list above:\n')
    if user_choice == str(1):
        get_owned(all_albums)
    elif user_choice == str(2):
        menu()
    else:
        print("Invalid input, please choose again!")


def search_menu():
    """
    Gives the user options to search the dataset
    """
    print("1 - search by album title")
    print("2 - search by year")
    print("3 - search by artist")
    print("4 - search by genre")
    user_choice = input("Please choose an option from the list above:\n")
    if user_choice == str(1):
        search.search_albums(all_albums, 2)
    elif user_choice == str(2):
        search.search_year(all_albums)
    elif user_choice == str(3):
        search.search_albums(all_albums, 3)
    elif user_choice == str(4):
        search.search_albums(all_albums, 4)
    else:
        print("Invalid input, please choose again!")


def print_top_100(album_data):
    """
    prints top 100 albums by ranking to terminal
    """
    trimmed_albums = []
    for i in album_data:
        album_list_trimed = i[:4]
        trimmed_albums.append(album_list_trimed)
    max_widths = [None, None, 35, 15]
    limited_data = trimmed_albums[:100]
    print(tabulate(limited_data,
          headers=["Ranking", "Year", "Album", "Artist"],
          tablefmt='grid', maxcolwidths=max_widths))



all_albums = get_albums()
menu()
