import csv
from tabulate import tabulate
import search
from owned import owned_album, print_owned, get_owned, remove_owned
from termcolor import colored, cprint


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
    max_widths = [None, None, 35, 20]
    print(tabulate(trimmed_album_data,
          headers=["Ranking", "Year", "Album", "Artist"],
          tablefmt='plain', maxcolwidths=max_widths))


def menu():
    """
    Prints user menu to screen
    """
    cprint("1 - Show all albums", "light_yellow")
    cprint("2 - Show top 100 albums", "light_yellow")
    cprint("3 - Show owned list", "light_yellow")
    cprint("4 - Search albums", "light_yellow")
    get_user_choice()


def get_user_choice():
    """
    Takes user input and directes user to their chossen selection
    """
    try:
        user_choice = int(input(colored('Please choose an option from the '
                                        'list above:\n',  "light_magenta")))
        if user_choice < 1 or user_choice > 4:
            raise ValueError
        if user_choice == 1:
            print_albums(trimmed_album_data)
            owned_menu()
        elif user_choice == 2:
            print_top_100(trimmed_album_data)
            owned_menu()
        elif user_choice == 3:
            print_owned(owned_album)
            owned_menu()
        elif user_choice == 4:
            search_menu()
        else:
            print("Invalid input, please choose again!")
            menu()
    except ValueError:
        cprint("Invalid input: Please choose a number between 1 and 4", "red")
        menu()


def owned_menu():
    """
    displays a menu to user to add album to owned list
    https://stackoverflow.com/questions/73663/how-do-i-terminate-a-script
    """
    cprint("1 - Add album to owned list", "light_yellow")
    cprint("2 - Remove album from owned list", "light_yellow")
    cprint("3 - Return to main menu", "light_yellow")
    cprint("4 - Exit", "light_yellow")
    try:
        user_choice = int(input(colored('Please choose an option from the '
                                        'list above:\n', "light_magenta")))
        if user_choice < 1 or user_choice > 4:
            raise ValueError
        if user_choice == 1:
            get_owned(trimmed_album_data)
            print_owned(owned_album)
            owned_menu()
        elif user_choice == 2:
            remove_owned()
            print_owned(owned_album)
            owned_menu()
        elif user_choice == 3:
            menu()
        elif user_choice == 4:
            exit()
        else:
            print("Invalid input, please choose again!")
            owned_menu()
    except ValueError:
        cprint("Invalid input: Please choose a number between 1 and 4", "red")
        owned_menu()


def search_menu():
    """
    Gives the user options to search the dataset
    """
    cprint("1 - search by album title", "light_yellow")
    cprint("2 - search by year", "light_yellow")
    cprint("3 - search by artist", "light_yellow")
    cprint("4 - search by genre", "light_yellow")
    try:
        user_choice = int(input(colored("Please choose an option from the "
                                        "list above:\n", "light_magenta")))
        if user_choice < 1 or user_choice > 4:
            raise ValueError
        if user_choice == 1:
            search.search_albums(all_albums, 2)
            owned_menu()
        elif user_choice == 2:
            search.search_year(all_albums)
            owned_menu()
        elif user_choice == 3:
            search.search_albums(all_albums, 3)
            owned_menu()
        elif user_choice == 4:
            search.search_albums(all_albums, 4)
            owned_menu()
        else:
            print("Invalid input, please choose again!")
            search_menu()
    except ValueError:
        cprint("Invalid input: Please choose a number between 1 and 4", "red")
        search_menu()


def print_top_100(trimmed_album_data):
    """
    prints top 100 albums by ranking to terminal
    """
    max_widths = [None, None, 35, 17]
    limited_data = trimmed_album_data[:100]
    print(tabulate(limited_data,
          headers=["Ranking", "Year", "Album", "Artist"],
          tablefmt='grid', maxcolwidths=max_widths))


def exit():
    """
    prints opening title and menu
    """
    opening_title()
    menu()


def opening_title():
    """
    Prints opening ascii art
    https://texteditor.com/ascii-art/
    """
    cprint("""
 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄ ▄▄▄     ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ 
█       █       █       █  █       █   █   █  ▄    █  █ █  █  █▄█  █       █
█▄     ▄█   ▄   █    ▄  █  █   ▄   █   █   █ █▄█   █  █ █  █       █  ▄▄▄▄▄█
  █   █ █  █ █  █   █▄█ █  █  █▄█  █   █   █       █  █▄█  █       █ █▄▄▄▄▄ 
  █   █ █  █▄█  █    ▄▄▄█  █       █   █▄▄▄█  ▄   ██       █       █▄▄▄▄▄  █
  █   █ █       █   █      █   ▄   █       █ █▄█   █       █ ██▄██ █▄▄▄▄▄█ █
  █▄▄▄█ █▄▄▄▄▄▄▄█▄▄▄█      █▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄█   █▄█▄▄▄▄▄▄▄█

    """, "light_magenta")


all_albums = get_albums()
trimmed_album_data = trimmed_albums(all_albums)
opening_title()
menu()
