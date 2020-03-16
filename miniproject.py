# Create a library class!
# display book.
# lend book (who owns the book,if not present)
# add book.
# return book.
# Aftab_Apu Library (list_book, Library_name)


class Library:
    def __init__(self, list , name):
        self.bookList = list
        self.name = name
        self.lendDict = {}


    def displayBook(self):
        print(f"we have following books in our library :{self.name}")
        for book in self.bookList:
                  print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("lend book database has been updated.You Can Take The Book Now")
        else:
            print(f"Book is already using by{self.lendDict[book]}")

    def addBook(self, book):
        self.bookList.append(book)
        print("Book has been added to the book list")
    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':

    aftab = Library(['PYTHON','C++','JAVA','C BASIC','ADVANCE_JAVA','C#'],"Code_with_Aftab")
    while(True):
        print(f"welcome to the {aftab.name}library.Enter your choice to continue")
        print("1.Display Book")
        print("2.Lend a Book")
        print("3.Add a Book")
        print("4.Return a Book")
        user_choice = input()

        if user_choice == '1':
            aftab.displayBook()
        elif user_choice == '2':
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your Name")
            aftab.lendBook(user, book)
        elif user_choice == '3':
            book = input("Enter the name of the book you want to add:")
            aftab.addBook(book)
        elif user_choice == '4':
            book = input("Enter the name of the book you want to return:")
            aftab.returnBook(book)

        else:
            print("Not a valid Option")

            print("Press to q quit and c to Continue")
            user_choice2 = ""
            while(user_choice2!="c" and user_choice2!="q"):
                user_choice2 = input()
                if user_choice2 == 'q':
                    exit()
                    if user_choice2 == 'c':
                        continue


