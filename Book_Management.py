
books={"allen B.Downey","Jeff Elkner","Chris Meyers","Luciano Ramalho"}
available_books={"allen B.Downey","Jeff Elkner","Chris Meyers","Luciano Ramalho","Mike MmGrath","David Griffiths","Dawn Griffiths","greg Perry"}
issue_books=set()
def available_book():
    #provided_book=books & available_books
    book=input("enter the book name").strip()
    if books & available_books: 
        print("=========THE AVAILABLE BOOKS======== \n",available_books)
        
    else:
       print("The books are not available")

#issue_books=set()

def issue_book():
    book=input("enter the book name").strip()
    if book in available_books:
        available_books.remove(book)
        issue_books.add(book)
        print("The",book,"book issued")
    
    else:
        print("The book is not issued")
        


def add_book():
    book=input("enter the book name").strip()
    if book in available_books:
        print("The book is already available")
    else:
        available_books.add(book)
        print("The",book,"successfully added to available book")

def return_book():
    book=input("enter the book name :").strip()
    if book in issue_books:
        available_books.add(book)
        issue_books.remove(book)
        print("The",book,"is return")
    else:
        print("The book is not return ")

def search_book():
    book=input("enter the book name :").strip()
    if book in available_books:
        print("the book is available")
    else:
        print("the book is not available")




while True:
    print("==========LIBRARY MANAGEMENT SYSTEM ========")
    
    print("1.Issue book")
    print("2. Add book")
    print("3. Available book")
    print("4. Return book")
    print("5. search book")
    print("6. EXIT")


    case=input("enter the case(1-5)")
    if case =='1':
        issue_book()
    elif case=="2":
        add_book()
    elif case=="3":
        available_book()
    elif case=="4":
        return_book()
    elif case=="5":
        search_book()
    elif case=="6":
        break
    
    else:
        print("please enter the valid book name ")
    







