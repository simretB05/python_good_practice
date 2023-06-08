import dbhelper

def get_all_books():
    results=dbhelper.run_procedure("call get_book()",[])
    print(results)

get_all_books() 

def get_book_by_author():
    author_name= input('add an author>>')

    result=dbhelper.run_procedure("call get_book_by_author(?)",[author_name])
    print(result)

get_book_by_author()  






