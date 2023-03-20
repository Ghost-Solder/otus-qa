import json
from csv import DictReader
from os import path

FILES_DIR = path.dirname('C:\\Users\\d.osipov\\Downloads\\')


def get_path(filename: str) -> str:
    return path.join(FILES_DIR, filename)


BOOKS_CSV_PATH = get_path('books.csv')
USERS_JSON_PATH = get_path('users.json')


def distribute_to_users(books_file_path: str, users_file_path: str):
    with (
        open(books_file_path, 'r', newline='') as books_file,
        open(users_file_path, 'r', newline='') as users_file,
    ):
        books = DictReader(books_file)
        users = json.load(users_file)

        users_iter = iter(users)

        result = {}

        for book in books:
            try:
                user = next(users_iter)
            except StopIteration:
                users_iter = iter(users)
                user = next(users_iter)

            book_data = {
                'title': book['Title'],
                'author': book['Author'],
                'pages': book['Pages'],
                'genre': book['Genre'],
            }

            if not result.get(user['name']):
                result[user['name']] = {
                    'name': user['name'],
                    'gender': user['gender'],
                    'address': user['address'],
                    'age': user['age'],
                    'books': [book_data],
                }
            else:
                result[user['name']]['books'].append(book_data)

        with open('result.json', 'w') as result_file:
            s = json.dumps(list(result.values()), indent=4)
            result_file.write(s)


if __name__ == '__main__':
    distribute_to_users(BOOKS_CSV_PATH, USERS_JSON_PATH)
