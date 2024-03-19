class Library:
    library_db = {}

    def __init__(self, title, author, unique_num, no_of_copies):
        self.title = title
        self.author = author
        self.unique_num = unique_num
        self.no_of_copies = no_of_copies

    def display(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nNumber: {self.unique_num}\nNo of copies: {self.no_of_copies}")

    def add_to_database(self):
        Library.library_db[self.unique_num] = {
            "title": self.title,
            "author": self.author,
            "unique_num": self.unique_num,
            "no_of_copies": self.no_of_copies
        }

    def take_a_book(self, unique_num, no_of_books=1):
        if unique_num in Library.library_db and Library.library_db[unique_num]["no_of_copies"] >= no_of_books:
            print(f"The book is available and you can take this by submitting the required documents.")
            Library.library_db[unique_num]["no_of_copies"] -= no_of_books
            print(f"The available copies of the book titled '{self.title}' is {Library.library_db[unique_num]['no_of_copies']}, after giving away {no_of_books} books.")
        else:
            print("The book is not available or does not have enough copies, please try again later.")

    def return_a_book(self, unique_num, no_of_books):
        if unique_num in Library.library_db:
            Library.library_db[unique_num]["no_of_copies"] += no_of_books
            print(f"The available copies of the book titled '{self.title}' is {Library.library_db[unique_num]['no_of_copies']}.")

# Example usage
book1 = Library("Python", "Chenchu", "123401", 20)
book2 = Library("Java", "Manohar", "123402", 20)
book3 = Library("JavaScript", "Krishna", "123403", 25)

book1.add_to_database()
book2.add_to_database()
book3.add_to_database()

book1.take_a_book("123401", 5)
