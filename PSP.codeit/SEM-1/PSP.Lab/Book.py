def count_books_by_title(book_catalog, title):
    ls = []
    count = 0
    for i in book_catalog :
        if i not in ls :
            ls.append(i)
        else:
            continue