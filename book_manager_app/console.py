import pdb 
from models.authors import Author
from models.books import Book
import repositories.author_repository as author_repository  
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()


author1 = Author("Stu")
author_repository.save(author1)

author2 = Author("Bon Jovi")
author_repository.save(author2)

author3 = Author("Mark Twain")
author_repository.save(author3)

book1 = Book("How to kill a mockingbird", "Rock", author2)
book_repository.save(book1)

book2 = Book("1984", "Dystopian", author1)
book_repository.save(book2)

book3 = Book("Moby Dick", "fiction", author3)
book_repository.save(book3)

pdb.set_trace()