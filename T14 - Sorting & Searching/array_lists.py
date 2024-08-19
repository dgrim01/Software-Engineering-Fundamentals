"""

"""

class Album:
    def __init__(self, album_name, album_artist, number_of_songs):
        self.album_name = album_name
        self.album_artist = album_artist
        self.number_of_songs = number_of_songs
        

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"
   
# Instances of the Album Object
albums1 = [

    Album("Reincarnate", "Motionless in White", 14),
    Album("Pendulum", "Twin Tribes", 10),
    Album("Alien", "Northlane", 11),
    Album("Sundowning", "Sleep Token", 12),
    Album("Shaman", "Orbit Culture", 5)
]
print("\nAlbums 1: ")
# Prints albums contained in the list albums1
for album in albums1:
    print(album)

albums1 = sorted(albums1, key=lambda album: album.number_of_songs) # sorts list album1 in order of number of songs

# Swapping elements at positions 1 and 2
swap = albums1[1]
albums1[1] = albums1[2]
albums1[2] = swap

print("\nAlbums 1 Sorted: ")
# Prints albums contained in the list albums1 after being sorted
for album in albums1:
    print(album)

albums2 = [

    Album("Body Machine","Priest", 10),
    Album("Lifeblood", "Brand of Sacrifice", 12),
    Album("In the Flat Fields", "Bauhaus", 18),
    Album("Let's Dance", "David Bowie", 8),
    Album("The Downward Spiral", "Nine Inch Nails", 14)
]

print("\nAlbums 2: ")
# Prints albums contained in the list albums2
for album in albums2:
    print(album)

# Adds albums from albums1 list to the albums2 list
for album in albums1:
    albums2.append(album)

print("\nAlbums 2 - Appended: ")
# Prints albums contained in the list albums2
for album in albums2:
    print(album)

# Added 2 elements to albums2 list
albums2.append(Album("Dark Side of the Moon", "Pink Floyd", 9))
albums2.append(Album("Oops!... I Did it Again", "Britney Spear", 16))

print("\nAlbums 2 - Add to 2 extra albums: ")
# Prints albums2 list with added elements
for album in albums2:
    print(album)

# Sorted Alphabetically
albums2 = sorted(albums2, key=lambda album: album.album_name)

print("\nAlbums 2 list 0 - Alphabetical order: ")
# Prints albums2 list in alphabetical order
for album in albums2:
    print(album)

def binary_search_album(albums, key):
    # Initialises left pointer of the list
    left = 0
    # Initialises right pointer of the list
    right = len(albums) -1
    # Loop until left pointer is less than right pointer
    while left <= right:
        # Calculates the middle index.
        mid = (left + right) // 2
        # If the middle element is equal to the key, return its index
        if albums[mid].album_name == key:

            return mid
        # If the middle element is less than the key, update left pointer to search the right half.
        elif albums[mid].album_name < key:

            left = mid + 1
        # If the middle element is greater than the key, update right pointer to search the left half.
        else:

            right = mid - 1
    # If the key is not found in the list, return -1.
    return -1

print("\nAlbum Search: ")
index = binary_search_album(albums2, "Dark Side of the Moon")
if index != -1:
    print(f"Album found at index: {index}")
    #print(albums2[index])
else:
    print("Dark Side of the Moon not found in the list")