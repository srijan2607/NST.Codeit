class book:
    def __init__(self,title , author,genre):
        self.title = title
        self.author = author
        self.genre = genre

book1 = book("Harry Potter", "J.K Rowling", "Fantasy")
book2 = book("Lord of the Rings", "J.R.R Tolkien", "Fantasy")
book3 = book("The Hobbit", "J.R.R Tolkien", "Fantasy")
print(book1.title)
print(book2.author)
print(book3.genre)