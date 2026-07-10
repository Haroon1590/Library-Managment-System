import json
from LibraryItems import Book, Magazine, DVD
from Member import Member


class Library:
    def __init__(self):
        self.catalog = []
        self.members = []

    def add_item(self, item):
        for existing in self.catalog:
            if existing.item_id == item.item_id:
                raise Exception("Item already in the catalog")
        self.catalog.append(item)

    def register_member(self, member):
        for existing in self.members:
            if existing.member_id == member.member_id:
                raise Exception("Member already in list")
        self.members.append(member)

    def borrow_item(self, member_id, item_id):
        found_member = None
        found_item = None

        for member in self.members:
            if member.member_id == member_id:
                found_member = member
                break

        for item in self.catalog:
            if item.item_id == item_id:
                found_item = item
                break

        if found_member is None:
            raise Exception("Member not found")
        if found_item is None:
            raise Exception("Item not found")

        found_item.borrow()
        found_member.add_borrowed(item_id)

    def return_item(self, member_id, item_id):
        found_member = None
        found_item = None

        for member in self.members:
            if member.member_id == member_id:
                found_member = member
                break

        for item in self.catalog:
            if item.item_id == item_id:
                found_item = item
                break

        if found_member is None:
            raise Exception("Member not found")
        if found_item is None:
            raise Exception("Item not found")

        found_item.return_item()
        found_member.remove_borrowed(item_id)

    def search(self, query):
        results = []
        query = query.lower()
        for item in self.catalog:
            if query in item.title.lower() or query in item.author.lower():
                results.append(item)
        return results

    def display_all(self):
        if not self.catalog:
            print("No items in catalog")
        for item in self.catalog:
            print(item)
            print("-" * 40)

    def save_data(self):
        items = []
        for item in self.catalog:
            d = item.to_dict()
            if isinstance(item, Book):
                d["type"] = "Book"
            elif isinstance(item, Magazine):
                d["type"] = "Magazine"
            elif isinstance(item, DVD):
                d["type"] = "DVD"
            items.append(d)

        with open("items.json", "w") as f:
            json.dump({"items": items}, f, indent=4)

        members = []
        for member in self.members:
            members.append(member.to_dict())

        with open("members.json", "w") as f:
            json.dump({"members": members}, f, indent=4)

    def load_data(self):
        try:
            with open("items.json", "r") as f:
                data = json.load(f)

            for item in data["items"]:
                if item["type"] == "Book":
                    book = Book(item["title"], item["author"], item["item_id"],
                                item["genre"], item["pages"])
                    book.is_available = item.get("is_available", True)
                    self.catalog.append(book)
                elif item["type"] == "Magazine":
                    magazine = Magazine(item["title"], item["author"], item["item_id"],
                                         item["issue_number"], item["month"])
                    magazine.is_available = item.get("is_available", True)
                    self.catalog.append(magazine)
                elif item["type"] == "DVD":
                    dvd = DVD(item["title"], item["author"], item["item_id"],
                              item["duration_mins"], item["director"])
                    dvd.is_available = item.get("is_available", True)
                    self.catalog.append(dvd)

        except FileNotFoundError:
            print("No saved items data found.")

        try:
            with open("members.json", "r") as f:
                data = json.load(f)

            for m in data["members"]:
                member = Member(m["name"], m["member_id"])
                member.borrowed_items = m.get("borrowed_items", [])
                self.members.append(member)

        except FileNotFoundError:
            print("No saved members data found.")

    def generate_report(self):
        report = "Library Report\n"
        report += "=" * 40 + "\n"
        report += "Catalog:\n"
        for item in self.catalog:
            report += str(item) + "\n"
            report += "-" * 40 + "\n"

        report += "Members:\n"
        for member in self.members:
            report += str(member) + "\n"
            report += "-" * 40 + "\n"

        return report


def library_menu():
    library = Library()
    library.load_data()

    while True:
        print("\nLibrary Management System")
        print("1. Add Item")
        print("2. Register Member")
        print("3. Borrow Item")
        print("4. Return Item")
        print("5. Search Items")
        print("6. Display All Items")
        print("7. Generate Report")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item_type = input("Enter item type (Book/Magazine/DVD): ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            item_id = input("Enter item ID: ")

            if item_type.lower() == "book":
                genre = input("Enter genre: ")
                pages = int(input("Enter number of pages: "))
                book = Book(title, author, item_id, genre, pages)
                library.add_item(book)
            elif item_type.lower() == "magazine":
                issue_number = input("Enter issue number: ")
                month = input("Enter month: ")
                magazine = Magazine(title, author, item_id, issue_number, month)
                library.add_item(magazine)
            elif item_type.lower() == "dvd":
                duration_mins = int(input("Enter duration in minutes: "))
                director = input("Enter director: ")
                dvd = DVD(title, author, item_id, duration_mins, director)
                library.add_item(dvd)
            else:
                print("Invalid item type.")

        elif choice == "2":
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            member = Member(name, member_id)
            library.register_member(member)

        elif choice == "3":
            member_id = input("Enter member ID: ")
            item_id = input("Enter item ID to borrow: ")
            try:
                library.borrow_item(member_id, item_id)
                print(f"Item {item_id} borrowed by member {member_id}.")
            except Exception as e:
                print(e)

        elif choice == "4":
            member_id = input("Enter member ID: ")
            item_id = input("Enter item ID to return: ")
            try:
                library.return_item(member_id, item_id)
                print(f"Item {item_id} returned by member {member_id}")
            except:
                print("An unexpected error occured")
        elif choice == "5":
            query = input("Enter search query: ")
            results = library.search(query)
            if not results:
                print("No items found")
            else:
                for item in results:
                    print(item)
                    print("-" * 40)
        elif choice == "6":
            library.display_all()
        elif choice == "7":
            report = library.generate_report()
            print(report)
        elif choice == "8":
            library.save_data()
            print("Exiting...")
            break
        else:
            print("Invalid input...")


library_menu()