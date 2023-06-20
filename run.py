import csv
from pprint import pprint
from tabulate import tabulate
import search
from owned import owned_album, print_owned, get_owned, remove_owned


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


def trimmed_albums(album_data):
    """
    Trims album list so as only ranking, year, 
    artist and album show in tables when displayed.
    """
    trimmed_albums = []
    for i in album_data:
        album_list_trimed = i[:4]
        trimmed_albums.append(album_list_trimed)
    return trimmed_albums


def print_albums(trimmed_album_data):
    """
    Prints all albums to screen minus subgenre and genre
    https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
    https://learnpython.com/blog/print-table-in-python/
    https://pypi.org/project/tabulate/
    """
    max_widths = [None, None, 35, 15]
    print(tabulate(trimmed_album_data,
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
            print_albums(trimmed_album_data)
            owned_menu()
        elif user_choice == str(2):
            print_top_100(trimmed_album_data)
            owned_menu()  
        elif user_choice == str(3):
            print_owned(owned_album)
            owned_menu()
        elif user_choice == str(4):
            search_menu()
        else:
            print("Invalid input, please choose again!")
            menu()
        


def owned_menu():
    """
    displayes a menu to user to add album to owned list
    """
    print("1 - Add album to owned list")
    print("2 - Remove album from owned list")
    print("3 - Return to main menu")
    user_choice = input('Please choose an option from the list above:\n')
    if user_choice == str(1):
        get_owned(trimmed_album_data)
        print_owned(owned_album)
        owned_menu()
    elif user_choice == str(2):
        remove_owned()
        print_owned(owned_album)
        owned_menu()
    elif user_choice == str(3):
        menu()
    else:
        print("Invalid input, please choose again!")
        owned_menu()


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
        owned_menu()
    elif user_choice == str(2):
        search.search_year(all_albums)
        owned_menu()
    elif user_choice == str(3):
        search.search_albums(all_albums, 3)
        owned_menu()
    elif user_choice == str(4):
        search.search_albums(all_albums, 4)
        owned_menu()
    else:
        print("Invalid input, please choose again!")
        search_menu()


def print_top_100(trimmed_album_data):
    """
    prints top 100 albums by ranking to terminal
    """
    max_widths = [None, None, 35, 15]
    limited_data = trimmed_album_data[:100]
    print(tabulate(limited_data,
          headers=["Ranking", "Year", "Album", "Artist"],
          tablefmt='grid', maxcolwidths=max_widths))


all_albums = get_albums()
trimmed_album_data = trimmed_albums(all_albums)
menu()
