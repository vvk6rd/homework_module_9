#DS5100 Module 08 Homework
#ID : VVK6RD
#Name: Ade Faparusi

import pandas as pd

class BookLover():
    """
    Just another Python class.
    """
   
    
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        

    def add_book(self, book_name, rating):
        self.book_name = book_name
        self.rating = rating
                
        if (len(self.book_list) > 0)  and (self.book_name in self.book_list.book_name.values):
            print(self.book_name, " already on book list")
            return False
        else:
            new_book = pd.DataFrame({
                'book_name': [self.book_name],
                'book_rating': [self.rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
 

    def has_read(self, book_name):
        self.book_name = book_name
        if self.book_name in self.book_list.book_name.values:
            print ("You have read the book: ", self.book_name)
            return True
        else: 
            print ("You have not read the book: ", self.book_name)
            return False
       
        
    def num_books_read(self):
        actual = len(self.book_list)
        print ('num_books_read: ', actual)
        return actual
        
    def fav_books(self):
        fav_list = [num for num in self.book_list[self.book_list.book_rating>3].book_name.values]
        print ("List of favorite books : ",fav_list)
        return fav_list
    
    
if __name__ == '__main__':

    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("Jane Eyre", 4)
    test_object.add_book("Fight Club", 3)
    test_object.add_book("The Divine Comedy", 5)
    test_object.add_book("The Popol Vuh", 5)
    test_object.has_read('The Popol Vuh')
    test_object.has_read('The Roll')
    test_object.num_books_read()
    test_object.fav_books()
    
    
    
    
    
    
    
    
    