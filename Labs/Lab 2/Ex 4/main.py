total_book_price = float(input("Enter the total book price: "))
numbers_of_books = int(input("Enter the number of books: "))

tax = total_book_price * 7.5 / 100
shipping_charge = 2 * numbers_of_books

total_charge = total_book_price + tax + shipping_charge

print(f"The total amount is {total_charge}")
