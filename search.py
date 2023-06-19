from tabulate import tabulate
import run


def search_albums(all_albums, album_row):
    """
    searches all album names by inputted word from user
    """
    search_word = input("Enter a search query:\n")
    found_albums = []
    for album in all_albums:
        if search_word.capitalize() in album[album_row]:
            found_albums.append(album[:4])

    if found_albums:
        max_widths = [None, None, 35, 15]
        print(tabulate(found_albums,
              headers=["Ranking", "Year", "Album", "Artist"],
              tablefmt='grid', maxcolwidths=max_widths))
        run.owned_menu()
    else:
        print("No albums found, please try again!")


def search_year(all_albums):
    """
    searched albums by year
    """
    year = input("Enter a search query:\n")
    found_albums = []
    for album in all_albums:
        if str(year) in album[1]:
            found_albums.append(album[:4])

    if found_albums:
        max_widths = [None, None, 35, 15]
        print(tabulate(found_albums,
              headers=["Ranking", "Year", "Album", "Artist"],
              tablefmt='grid', maxcolwidths=max_widths))
        run.owned_menu()
    else:
        print("No albums found, please try again!")
