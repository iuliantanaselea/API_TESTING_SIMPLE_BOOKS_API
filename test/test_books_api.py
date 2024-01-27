from api_requests.books_requests import *


class TestBooksApi:

    def test_get_all_books_status_code(self):
        response = get_all_books()
        status_code = response.status_code
        assert status_code == 200, "The request failed"

    def test_get_all_books_response_body(self):
        response = get_all_books()
        books = response.json()
        for book in books:
            print(book.keys())
            assert 'id' in book.keys()
            assert 'name' in book.keys()
            assert 'type' in book.keys()
            assert 'available' in book.keys()

    def test_get_all_fiction_books(self):
        response = get_all_books(filter_type="fiction")
        fiction_books = response.json()
        for book in fiction_books:
            assert book['type'] == "fiction"

    def test_get_all_non_fiction_books(self):
        response = get_all_books(filter_type="non-fiction")
        fiction_books = response.json()
        for book in fiction_books:
            assert book['type'] == "non-fiction"

    def test_get_first_3_books(self):
        response = get_all_books(limit=3)
        books = response.json()
        assert len(books) <= 3, "Number of books should be max 3"

    def test_get_one_book(self):
        response = get_all_books(limit=1)
        books = response.json()
        assert len(books) <= 1, "Number of books should be max 1"

    def test_max_value_for_limit(self):
        response = get_all_books(limit=20)
        books = response.json()
        assert len(books) <= 20, "Number of books should be max 20"

    # test introducing type=comedy
    def test_invalid_type_value(self):
        response = get_all_books(filter_type="comedy")
        assert response.status_code == 400
        assert response.json()[
                   'error'] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."

    def test_negative_limit_value(self):
        response = get_all_books(limit=-1)
        assert response.status_code == 400
        error = response.json()['error']
        assert error == "Invalid value for query parameter 'limit'. Must be greater than 0."

    def test_limit_value_greater_than_20(self):
        response = get_all_books(limit=21)
        error = response.json()['error']
        assert error == "Invalid value for query parameter 'limit'. Cannot be greater than 20."
