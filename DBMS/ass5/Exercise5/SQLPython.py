import sqlite3


def createDB(conn, c):
    try:
        c.execute('''CREATE TABLE Albums (
                    albumName TEXT NOT NULL,
                    companyName TEXT REFERENCES Companies(companyName),
                    year INTEGER,
                    length INTEGER,
                    genre TEXT CHECK (genre IN ("pop", "rock", "jazz", "classical", "folk")),
                    PRIMARY KEY (albumName, companyName)
                    )''')
        c.execute('''CREATE TABLE Companies (
                    companyName TEXT NOT NULL,
                    country TEXT DEFAULT "USA",
                    webpage TEXT NOT NULL,
                    PRIMARY KEY (companyName)
                    )''')
        c.execute('''CREATE TABLE Artists (
                    artistName TEXT PRIMARY KEY,
                    gender TEXT CHECK (gender IN ("F", "M", "O")),
                    born INTEGER
                    )''')
        c.execute('''CREATE TABLE Tracks (
                    trackNo INTEGER CHECK (trackNo > 0 AND trackNo < 100),
                    albumName TEXT NOT NULL,
                    companyName TEXT NOT NULL,
                    trackName TEXT,
                    artistName TEXT NOT NULL,
                    composer TEXT,
                    lyricist TEXT,
                    length INTEGER,
                    FOREIGN KEY(albumName, companyName) REFERENCES Albums(albumName, companyName),
                    FOREIGN KEY (artistName) REFERENCES Artists(artistName)
                    );''')

        c.execute('''INSERT INTO Artists(artistName, gender, born)
                    VALUES("Celine Dion", "F", 1963
                    )''')

        conn.commit()
        print("Database created")

    except sqlite3.OperationalError:
        print("Connected to database")


def getInput(conn, c):
    mod = input("\nInput command: C = Add Company / A = Add Album / S = Search / Q = Quit\n")
    while mod != 'Q':
        if mod == 'C':
            infoText = input("Insert Company: Write company info, separate fields with spaces\n")
            info = infoText.split()
            insert = "INSERT INTO Companies VALUES(?, ?, ?)"
            c.execute(insert, (info[0], info[1], info[2]))
            conn.commit()
            print("\nInserted", info[0])
        if mod == 'A':
            infoText = input("Insert Album: Write album info, separate fields with spaces\n")
            info = infoText.split()
            insert = "INSERT INTO Albums VALUES(?, ?, ?, ?, ?)"
            c.execute(insert, (info[0], info[1], info[2], info[3], info[4]))
            conn.commit()
            print("\nInserted", info[0])
        if mod == 'S':
            info = input("Search Company: Write company name\n")
            search = "SELECT albumName, year, genre FROM Albums WHERE companyName = ?"
            c.execute(search, (info,))
            rows = c.fetchall()
            print("\nAlbums published by", info)
            for row in rows:
                print(row[0], row[1], row[2])
        mod = input("\nInsert command: C = Add Company / A = Add Album / S = Search / Q = Quit\n")


def main():
    conn = sqlite3.connect("musicalbums.db")
    c = conn.cursor()
    createDB(conn, c)
    
    c.execute("SELECT born FROM Artists WHERE artistName = 'Celine Dion'")
    year = c.fetchone()
    print("The year is", year[0])


    getInput(conn, c)    

    print("EXITING")
    conn.close()


if __name__ == '__main__':
    main()
