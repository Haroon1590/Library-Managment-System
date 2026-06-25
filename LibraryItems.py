class LibraryItem:
    def __init__(self,title, author, item_id):
        self.title=title
        self.author=author
        self.item_id=item_id


    def __str__(self):
        return f"title : {self.title} \nAuthor : {self.author}\nItem_Id : {self.item_id}"
    
class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre, pages):
        super().__init__(title, author, item_id)
        self.genre=genre
        self.pages=pages
        self.is_available=True
        
    
    def borrow(self):
        if self.is_available:
            self.is_available=False
        else:
            raise Exception("Item already Borrowed")
    
    def return_book(self):
        self.is_available=True

    def to_dict(self):
        return self.__dict__
    
    def __str__(self):
        return super().__str__()+f"\nGenre : {self.genre}  \nPages : {self.pages} \nAvailabillity : {self.is_available}"
    

    