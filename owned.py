from tabulate import tabulate
from termcolor import colored, cprint

owned_album = []


def get_owned(trimmed_album_data):
    """
    gets album from list based on user input and returns album
    and artist in string format, then appends to new list owned_albums
    https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
    """
    while True:
        try:
            album_ranking = int(input(colored("Please input the ranking of the album you would "
                          "like to add:\n", "light_magenta")))
            if album_ranking < 1 or album_ranking > 500:
                raise ValueError
            selected_album = trimmed_album_data[album_ranking -1]
            if selected_album not in owned_album:
                owned_album.append(selected_album)
                break
            else:
                cprint("Album already in list!", "red")
                break
        except ValueError:
            cprint("Invalid input: Please enter a number between 1 and 500" , "red")


def print_owned(owned_album):
    """
    Prints to screen users owned albums
    https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
    """
    if not owned_album:
        cprint("You have not added anything to this list yet!" , "red")  
    else:
        max_widths = [None, None, 35, 15]
        print(tabulate(owned_album,
              headers=["Ranking", "Year", "Album", "Artist"],
              tablefmt='grid', maxcolwidths=max_widths))


def remove_owned():
    """
    Removes album for list of owned albums
    https://datagy.io/python-list-pop-remove-del-clear/
    https://stackoverflow.com/questions/9553638/find-the-index-of-an-item-in-a-list-of-lists
    https://www.w3schools.com/python/ref_func_reversed.asp
    """
    try:
        if not owned_album:
            cprint("You have not added anything to this list yet!" , "red")  
        else:
            album_ranking = input(colored("Please input the ranking of the album you would "
                          "like to remove:\n", "light_magenta"))
        if int(album_ranking) < 1 or int(album_ranking) > 500:
            raise ValueError
        removed_albums = []
        for i, album in enumerate(owned_album):
            if album_ranking in album:
                removed_albums.append(i)
            else:
                cprint("Album not in owned list!" , "red")
        for index in reversed(removed_albums):
            owned_album.pop(index)
    except ValueError:
        cprint("Invalid input: Please enter a number between 1 and 500" , "red") 
