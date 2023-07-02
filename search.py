from tabulate import tabulate
from termcolor import colored, cprint


def search_albums(all_albums, album_row):
    """
    searches all album names by inputted word from user
    """
    while True:
        try:
            search_word = input(colored("Enter a search query:\n", "light_magenta"))
            if search_word == "":
                raise ValueError
            found_albums = []
            for album in all_albums:
                if search_word.capitalize() in album[album_row]:
                    found_albums.append(album[:4])
            if found_albums:
                max_widths = [None, None, 35, 25]
                print(tabulate(found_albums,
                      headers=["Ranking", "Year", "Album", "Artist"],
                      tablefmt='grid', maxcolwidths=max_widths))
                break
            else:
                cprint("No albums found, please try again!", "red")
        except ValueError:
            cprint("Invalid input: Input cannot be empty", "red")


def search_year(all_albums):
    """
    searched albums by year
    """
    while True:
        try:
            year = int(input(colored("Please input a year from 1955 to 2011:\n", "light_magenta")))
            if year < 1955 or year > 2011:
                raise ValueError
            found_albums = []
            for album in all_albums:
                if str(year) in album[1]:
                    found_albums.append(album[:4])
            if found_albums:
                max_widths = [None, None, 35, 20]
                print(tabulate(found_albums,
                      headers=["Ranking", "Year", "Album", "Artist"],
                      tablefmt='grid', maxcolwidths=max_widths))
                break
            else:
                cprint("No albums found, please try again!", "red")
        except ValueError:
            cprint("Invalid input: Please try again!", "red")
