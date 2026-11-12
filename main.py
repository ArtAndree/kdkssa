import csv
from pathlib import Path
from pprint import pprint


def get_books(filename):
    """Прочитать книги, преобразовав количество и цену в числа."""
    with open(filename, encoding="utf-8", newline="") as file:
        rows = csv.reader(file, delimiter="|")
        next(rows, None)
        return list(map(
            lambda row: [row[0], row[1], row[2], int(row[3]), float(row[4])],
            rows,
        ))


def filtered_books(books, title):
    """Выбрать книги по подстроке в названии без учёта регистра."""
    selected = filter(lambda book: title.lower() in book[1].lower(), books)
    return list(map(
        lambda book: [book[0], book[1] + ", " + book[2], book[3], book[4]],
        selected,
    ))


def get_total(books):
    """Получить ISBN и стоимость всех экземпляров выбранных книг."""
    return list(map(lambda book: (book[0], book[2] * book[3]), books))


if __name__ == "__main__":
    books = get_books(Path(__file__).with_name("books.csv"))
    print("Все книги:")
    pprint(books)
    selected_books = filtered_books(books, "python")
    print("\nКниги о Python:")
    pprint(selected_books)
    print("\nСтоимость всех экземпляров выбранных книг:")
    pprint(get_total(selected_books))
