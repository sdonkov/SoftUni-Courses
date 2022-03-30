book_wanted=input()

books_count=0

book=input()

while book_wanted!=book:
    book=input()
    books_count+=1
    if book=="No More Books":
        print("The book you search is not here!")
        print(f"You checked {books_count} books.")
        break
if book==book_wanted:
    print(f"You checked {books_count} books and found it.")




    # print(book_wanted)
