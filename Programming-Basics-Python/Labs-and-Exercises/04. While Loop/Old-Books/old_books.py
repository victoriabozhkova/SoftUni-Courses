wanted_book = input()

books_count = 0
current_book = input()
book_is_found = False

while current_book != "No More Books":
    if current_book == "No More Books":
        break

    if current_book == wanted_book:
        book_is_found = True
        break

    books_count += 1
    current_book = input()

if book_is_found == True:
    print(f"You checked {books_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_count} books.")