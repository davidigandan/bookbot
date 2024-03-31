from collections import Counter

with open('/Users/davidigandan/working_directory/BookBot Project/bookbot/books/Project_Gutenbergs_Frankenstein.txt') as book:
    book_contents = book.read()
    print('Length of book contents: ' + str(len(book_contents)))
    book_as_w_list=book_contents.split()

    uniques = set(book_contents.lower())
    print(len("Number of uniques: " + str(uniques)))

    opus = Counter(book_contents.lower())
    print(opus)


    book.close()