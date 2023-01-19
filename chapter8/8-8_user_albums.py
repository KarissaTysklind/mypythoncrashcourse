def make_album(artist_name, album_title, num_tracks = ""):
    album = {"artist": artist_name, "title": album_title}
    if num_tracks != "":
        album["tracks"] = num_tracks
    return album

while True:
    print("\nPlease enter album details")
    print("(enter 'q' at any time to quit)\n")

    artist_name = input("artist name: ")
    if artist_name == 'q':
        break
    album_title = input("album title: ")
    if album_title == 'q':
        break
    album = make_album(artist_name, album_title)
    
print(album)
