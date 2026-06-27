class Member:
    def __init__(self, name, member_id):
        self.name=name
        self.member_id=member_id
        self.borrowed_items=[]
    
    def add_borrowed(self,item_id):
        self.borrowed_items.append(item_id)
    def remove_borrowed(self,item_id):
        self.borrowed_items.remove(item_id)
    def to_dict(self):
        return self.__dict__
    def __str__(self):
        return f"Name : {self.name}\nMember ID : {self.member_id}\nBorrowed items : {self.borrowed_items}"
        