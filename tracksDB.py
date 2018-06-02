import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('tracks.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Artist')
cur.execute ('DROP TABLE IF EXISTS Genre')
cur.execute('DROP TABLE IF EXISTS Album')
cur.execute('DROP TABLE IF EXISTS Track')

cur.execute('''CREATE TABLE Artist
           (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
           name TEXT UNIQUE )
           ''')
cur.execute('''CREATE TABLE Genre
            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name TEXT UNIQUE)
            ''')
cur.execute(''' CREATE TABLE Album
             (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
             artist_id INTEGER,
             title TEXT UNIQUE)
             ''')
cur.execute(''' CREATE TABLE Track
            (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            title TEXT UNIQUE,
            album_id INTEGER,
            genre_id INTEGER,
            len INTEGER,
            rating INTEGER,
            count INTEGER)
            ''')

fn = input('Enter xml file name: ')
if len(fn) < 1 : fn = 'Library.xml'
fhand = open(fn)

def lookup(d,key):
    found = False
    for child in d:
        if found == True: return child.text
        if child.tag == 'key' and child.text == key:
            found =True
    return None

stuff = ET.parse(fhand)
#creat list of dictionaries - each dics has all information about each track
all_tracks = stuff.findall('dict/dict/dict')


#print(lookup(all_tracks[3],'Name'))
#print(all_tracks[3][3].text)
#print(all_tracks[3][17].text)
#print(all_tracks[3][47].text)
#print(all_tracks[3][37].text)
#print(all_tracks[3][5].text)
#print(all_tracks[3][9].text)
#print(all_tracks[3][11].text)

for track in all_tracks:

    #print(lookup (track,'Track ID'))
    if (lookup(track,'Track ID') is None ): continue

    title = lookup(track,'Name')
    length = lookup(track,'Total Time')
    rating = lookup(track,'Rating')
    count = lookup(track, 'Play Count')
    artist = lookup(track,'Artist')
    album = lookup(track,'Album')
    genre = lookup(track,'Genre')

    #print(title, artist, album, genre, count, rating, length)

    if title is None or artist is None or album is None or genre is None :  continue

    print(title, artist, album, genre, count, rating, length)

    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?',(genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name =?',(artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Album (artist_id,title) VALUES (?,?)',(artist_id,album))
    cur.execute('SELECT id FROM Album WHERE title = ?',(album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Track (title, album_id, genre_id, len,rating, count)
                VALUES (?,?,?,?,?,?)''',(title , album_id, genre_id,length,rating,count) )
    conn.commit()
