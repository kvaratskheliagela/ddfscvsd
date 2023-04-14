#1 davaleba
# import sqlite3
#
# # ბაზის შექმნა
# conn = sqlite3.connect('books_db.db')
#
# # ცხრილის შექმნა
# conn.execute('''CREATE TABLE books
#              (book_id INTEGER PRIMARY KEY AUTOINCREMENT,
#              title TEXT NOT NULL,
#              author TEXT NOT NULL,
#              release_year INTEGER NOT NULL,
#              price REAL NOT NULL);''')
#
# # ჩანაწერის დამატება
# conn.execute("INSERT INTO books (title, author, release_year, price) \
#              VALUES ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 9.99)")
#
# # ერთდროულად 4 ჩანაწერის დამატება
# books = [('To Kill a Mockingbird', 'Harper Lee', 1960, 12.99),
#          ('1984', 'George Orwell', 1949, 8.99),
#          ('Pride and Prejudice', 'Jane Austen', 1813, 7.99),
#          ('The Catcher in the Rye', 'J.D. Salinger', 1951, 11.99)]
#
# conn.executemany("INSERT INTO books (title, author, release_year, price) \
#                  VALUES (?, ?, ?, ?)", books)
#
# # ბაზის დახურვა
# conn.commit()
# conn.close()
#davaleba 2
# import sqlite3
#
# conn = sqlite3.connect('titanic.db')
# c = conn.cursor()
# data = ('John Smith', 25, 'male', 'ABC123', 'C42')
# passengers = [
#     ('Jane Doe', 22, 'female', 'DEF456', 'D27'),
#     ('Mark Johnson', 30, 'male', 'GHI789', 'E31'),
#     ('Sarah Lee', 18, 'female', 'JKL012', 'F15')
# ]
# c.executemany('INSERT INTO passengers (passenger_name, age, sex, ticket, cabin) VALUES (?, ?, ?, ?, ?)', passengers)
#
# conn.commit()
# conn.close()
#davaleba3
import sqlite3
class Movie:
    def __init__(self, title, genre, year, imdb):
        self.title = title
        self.genre = genre
        self.year = year
        self.imdb = imdb

    def __str__(self):
        return f"Title: {self.title}, Genre: {self.genre}, Year: {self.year}, IMDB: {self.imdb}"

conn = sqlite3.connect('movies.db')
c = conn.cursor()
c.execute('''CREATE TABLE movies
             (movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
             title TEXT,
             genre TEXT,
             year INTEGER,
             imdb REAL)''')

movie = Movie('The Shawshank Redemption', 'Drama', 1994, 9.3)
c.execute("INSERT INTO movies (title, genre, year, imdb) VALUES (?, ?, ?, ?)", (movie.title, movie.genre, movie.year, movie.imdb))

conn.commit()
conn.close()

