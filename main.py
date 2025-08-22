class Node:
    def __init__(self, id, book_name, author, genre=None, year=None):
        self.id = id
        self.book_name = book_name
        self.author = author
        self.genre = genre
        self.year = year
        self.left = None
        self.right = None
        
    def insert(self, root, n, book_name, author, genre=None, year=None):
        if n < root.id:
            if root.left is None:
                root.left = Node(n, book_name, author, genre, year)
            else:
                self.insert(root.left, n, book_name, author, genre, year)
        elif n > root.id:
            if root.right is None:
                root.right = Node(n, book_name, author, genre, year)
            else:
                self.insert(root.right, n, book_name, author, genre, year)
                
    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current
        
    def delete(self, root, n):
        if root is None:
            return None
        if n < root.id:
            root.left = self.delete(root.left, n)
        elif n > root.id:
            root.right = self.delete(root.right, n)
        else:
            # 0 child
            if root.left is None and root.right is None:
                return None
            # 1 child
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # 2 children
            minimum = self.find_min(root.right)
            # Copy all data from the minimum node
            root.id = minimum.id
            root.book_name = minimum.book_name
            root.author = minimum.author
            root.genre = minimum.genre
            root.year = minimum.year
            root.right = self.delete(root.right, minimum.id)
        return root
        
    def search(self, root, n):
        if root is None:
            return None
        if n < root.id:
            return self.search(root.left, n)
        elif n > root.id:
            return self.search(root.right, n)
        else:
            return root
            
    def search_by_name(self, root, name):
        results = []
        if root:
            if root.book_name.lower() == name.lower():
                results.append(root)
            results.extend(self.search_by_name(root.left, name))
            results.extend(self.search_by_name(root.right, name))
        return results
        
    def search_by_author(self, root, author):
        results = []
        if root:
            if root.author.lower() == author.lower():
                results.append(root)
            results.extend(self.search_by_author(root.left, author))
            results.extend(self.search_by_author(root.right, author))
        return results
        
    def preorder(self, root):
        if root:
            print(f"ID: {root.id}, Title: {root.book_name}, Author: {root.author}", end=" | ")
            self.preorder(root.left)
            self.preorder(root.right)
            
    def display_book_details(self):
        print(f"\nBook Details:")
        print(f"ID: {self.id}")
        print(f"Title: {self.book_name}")
        print(f"Author: {self.author}")
        if self.genre:
            print(f"Genre: {self.genre}")
        if self.year:
            print(f"Year: {self.year}")

class Node:
    def __init__(self, id, book_name, author, genre=None, year=None):
        self.id = id
        self.book_name = book_name
        self.author = author
        self.genre = genre
        self.year = year
        self.left = None
        self.right = None
        
    def insert(self, root, n, book_name, author, genre=None, year=None):
        if n < root.id:
            if root.left is None:
                root.left = Node(n, book_name, author, genre, year)
            else:
                self.insert(root.left, n, book_name, author, genre, year)
        elif n > root.id:
            if root.right is None:
                root.right = Node(n, book_name, author, genre, year)
            else:
                self.insert(root.right, n, book_name, author, genre, year)
                
    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current
        
    def delete(self, root, n):
        if root is None:
            return None
        if n < root.id:
            root.left = self.delete(root.left, n)
        elif n > root.id:
            root.right = self.delete(root.right, n)
        else:
            # 0 child
            if root.left is None and root.right is None:
                return None
            # 1 child
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # 2 children
            minimum = self.find_min(root.right)
            # Copy all data from the minimum node
            root.id = minimum.id
            root.book_name = minimum.book_name
            root.author = minimum.author
            root.genre = minimum.genre
            root.year = minimum.year
            root.right = self.delete(root.right, minimum.id)
        return root
        
    def search(self, root, n):
        if root is None:
            return None
        if n < root.id:
            return self.search(root.left, n)
        elif n > root.id:
            return self.search(root.right, n)
        else:
            return root
            
    def search_by_name(self, root, name):
        results = []
        if root:
            if name.lower() in root.book_name.lower():  # Partial match instead of exact match
                results.append(root)
            results.extend(self.search_by_name(root.left, name))
            results.extend(self.search_by_name(root.right, name))
        return results
        
    def search_by_author(self, root, author):
        results = []
        if root:
            if root.author.lower() == author.lower():
                results.append(root)
            results.extend(self.search_by_author(root.left, author))
            results.extend(self.search_by_author(root.right, author))
        return results
        
    def preorder(self, root):
        if root:
            print(f"ID: {root.id}, Title: '{root.book_name}', Author: {root.author}")
            self.preorder(root.left)
            self.preorder(root.right)
            
    def display_book_details(self):
        print(f"\nBook Details:")
        print(f"ID: {self.id}")
        print(f"Title: {self.book_name}")
        print(f"Author: {self.author}")
        if self.genre:
            print(f"Genre: {self.genre}")
        if self.year:
            print(f"Year: {self.year}")
        print("-" * 30)

# Create a library with sample books
library = Node(101, "The Great Gatsby", "F. Scott Fitzgerald", "Classic", 1925)

# Add more books to the library
library.insert(library, 205, "To Kill a Mockingbird", "Harper Lee", "Fiction", 1960)
library.insert(library, 87, "1984", "George Orwell", "Dystopian", 1949)
library.insert(library, 302, "Pride and Prejudice", "Jane Austen", "Romance", 1813)
library.insert(library, 150, "The Hobbit", "J.R.R. Tolkien", "Fantasy", 1937)
library.insert(library, 275, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy", 1997)
library.insert(library, 50, "The Catcher in the Rye", "J.D. Salinger", "Fiction", 1951)
library.insert(library, 400, "The Lord of the Rings", "J.R.R. Tolkien", "Fantasy", 1954)
library.insert(library, 180, "Brave New World", "Aldous Huxley", "Dystopian", 1932)
library.insert(library, 225, "The Da Vinci Code", "Dan Brown", "Mystery", 2003)
library.insert(library, 320, "The Alchemist", "Paulo Coelho", "Adventure", 1988)
library.insert(library, 125, "The Shining", "Stephen King", "Horror", 1977)
library.insert(library, 350, "The Hunger Games", "Suzanne Collins", "Dystopian", 2008)

# Display all books in the library
print("All books in the library (Preorder traversal):")
print("=" * 60)
library.preorder(library)

# Search for books by author
print("\n\nSearching for books by J.R.R. Tolkien:")
print("=" * 40)
tolkien_books = library.search_by_author(library, "J.R.R. Tolkien")
for book in tolkien_books:
    book.display_book_details()

# Search for books by title
print("\nSearching for books with 'The' in title:")
print("=" * 40)
the_books = library.search_by_name(library, "The")
for book in the_books:
    book.display_book_details()

# Search for dystopian books
print("\nSearching for dystopian books:")
print("=" * 40)
dystopian_books = []
for book in [library.search(library, 87), library.search(library, 180), library.search(library, 350)]:
    if book and book.genre == "Dystopian":
        dystopian_books.append(book)

for book in dystopian_books:
    book.display_book_details()

# Delete a book
print("\nDeleting 'The Da Vinci Code' (ID: 225):")
print("=" * 40)
library = library.delete(library, 225)

# Verify deletion by showing all books again
print("\nAll books after deletion:")
print("=" * 40)
library.preorder(library)