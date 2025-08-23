# Library Management System with Binary Search Tree

A Python application that manages a library catalog using a Binary Search Tree data structure. This system efficiently handles book operations like adding, removing, and searching through the collection.

## ✨ What It Does

- **Manage Books**: Easily add and remove books from your library
- **Smart Searching**: Find books by ID, title, or author
- **Organized Storage**: Books are automatically sorted by ID for quick access
- **Detailed Info**: Store book titles, authors, genres, and publication years

## 📚 How It Works

Each book becomes a node in the binary search tree, organized by its unique ID. This makes searching and managing books super efficient!

### What's Stored for Each Book:
- `id` - Unique book identifier (the main sorting key)
- `book_name` - The title of the book
- `author` - Who wrote it
- `genre` - What type of book it is (optional)
- `year` - When it was published (optional)

## 🚀 Getting Started

### What You Need
- Python 3.x (any recent version will work)

### Quick Setup
1. **Save the code** to a file (maybe call it `library_manager.py`)
2. **Run it** with:
   ```bash
   python library_manager.py
   ```

### Try It Out
The system comes pre-loaded with popular books so you can test it right away. Here's what you can do:

```python
# The system automatically creates a starter library
# You'll see books like "1984", "The Great Gatsby", and Harry Potter

# Look up books by author
author_books = library.search_by_author(library, "J.R.R. Tolkien")

# Find books by title (even partial names work!)
title_books = library.search_by_name(library, "The")

# See everything in your library
library.preorder(library)
```

## 🛠️ Under the Hood

### Main Features:
- **Add Books**: New books get placed in the right spot automatically
- **Remove Books**: Delete books while keeping everything organized
- **Find Books**: Quick searches by ID, title, or author
- **Browse All**: See your entire collection in order

### How Fast Is It?
- **Adding books**: Usually fast (logarithmic time)
- **Finding books**: Quick search through the tree
- **Deleting books**: Efficient removal with tree maintenance

## 💡 Real-World Uses

This isn't just a school project - it shows how binary trees work in:
- Actual library systems
- Store inventory management
- Database systems
- Anywhere you need quick search and organization

## 🔮 What Could Be Next

This is a solid foundation, but there's always room to grow:
- More ways to view books (different sorting orders)
- Save your library to a file
- Add a simple menu interface
- More search options (by genre, year, etc.)
- Track which books are borrowed

## 📄 License

Free to use and modify - this is open source under the MIT License.

---

**Ready to try it?** Just run the code and start exploring your new digital library! The example books give you a great starting point to see how everything works.
