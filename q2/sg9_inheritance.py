class Publication:  # created a parent class
    def __init__(self, title: str, author: str):
        self.__title = title
        self.__author = author
    
    # getter method for title    
    def get_title(self):
        return self.__title

    # getter method for author
    def get_author(self):
        return self.__author
    
    # setter method for title
    def set_title(self, title: str):
        self.__title = title

    # setter method for author
    def set_author(self, author: str):
        self.__author = author
        
    # method to display info about the publication
    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        
class Book(Publication):  # created a child class of Publication
    def __init__(self, title: str, author: str, number_pages: int):
        super().__init__(title, author)
        self.__number_pages = number_pages

    # getter method for no. of pages
    def get_number_of_pages(self):
        return self.__number_pages

    # setter method for no. of pages
    def set_number_of_pages(self, number_of_pages: int):
        if number_of_pages < 0:
            print("Number of pages must be positive.")
            return
        else:
            self.__number_pages = number_of_pages

    # method to display info about the book
    def display_info(self):
        super().display_info()
        print(f"Number of Pages: {self.__number_pages}")
        
class Magazine(Publication):  # created another child class of Publication
    def __init__(self, title: str, author: str, issue_number: int):
        super().__init__(title, author)
        self.__issue_number = issue_number

    # getter method for issue number
    def get_issue_number(self):
        return self.__issue_number

    # setter method for issue number
    def set_issue_number(self, issue_number: int):
        self.__issue_number = issue_number

    # method to display info about the magazine
    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.__issue_number}")
        
# Creating objects
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkein", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

# printing the information of the objects
print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)  # setting invalid value
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())
