class LibraryItem:
    def __init__(self,title, author, item_id):
        self.title=title
        self.author=author
        self.item_id=item_id
        self.is_available=True


    def __str__(self):
        return f"title : {self.title}\nAuthor : {self.author}\nItem_Id : {self.item_id}"
    
    def borrow(self):
        if self.is_available:
            self.is_available=False
        else:
            raise Exception("Item already Borrowed")
    
    def return_item(self):
        self.is_available=True

    def to_dict(self):
        return dict(self.__dict__)
    
    
    
class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre, pages):
        super().__init__(title, author, item_id)
        self.genre=genre
        self.pages=pages
        
    def __str__(self):
        return super().__str__()+f"\nGenre : {self.genre}  \nPages : {self.pages} \nAvailabillity : {self.is_available}"
    
class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number, month):
        super().__init__(title, author, item_id)
        self.issue_number=issue_number
        self.month=month
        
    def __str__(self):
        return super().__str__()+f"\nIssue Number : {self.issue_number}\nMonth : {self.month}\nAvailability : {self.is_available}"

class DVD(LibraryItem):
    def __init__(self, title, author, item_id, duration_mins, director):
        super().__init__(title, author, item_id)
        self.duration_mins=duration_mins
        self.director=director
    
    def __str__(self):
        return super().__str__()+f"\nDirector :{self.director}\nDuration : {self.duration_mins}\nAvailabillity : {self.is_available}"