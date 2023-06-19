from tabulate import tabulate
import run

owned_album = []


def get_owned(trimmed_album_data):
    """
    gets album from list based on user input and returns album
    and artist in string format, then appends to new list owned_albums
    https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
    """
    album_ranking = input("Please input the ranking of the album you would \
                           like to add:\n")
    selected_album = trimmed_album_data[int(album_ranking)-1]
    owned_album.append(selected_album)
    run.menu()
    return owned_album


def print_owned(owned_album):
    """
    Prints to screen users owned albums
    https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty
    """
    if not owned_album:
        print("You have not added anything to this list yet!")
        run.owned_menu()
    else:
        max_widths = [None, None, 35, 15]
        print(tabulate(owned_album,
              headers=["Ranking", "Year", "Album", "Artist"],
              tablefmt='grid', maxcolwidths=max_widths))
        run.owned_menu()
