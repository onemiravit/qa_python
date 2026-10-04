import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2    # исправлен метод get_books_rating, которого нет в классе BooksCollector

    @pytest.mark.parametrize('name', [          # Применяем параметризацию для проверки добавления названия книги в 1 и 40 символов
        'Я',                                    # В этом тесте сразу 3 проверки
        'Яндекс книга лучшая книга для развития !'
    ])
    def test_add_new_book_valid_name_book_added(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)            # Добавляем название книги

        assert name in collector.get_books_genre() # Проверяем добавленные книги
    
    @pytest.mark.parametrize('name', [          # Применяем параметризацию для проверки, что книги не добавляются
        '',                                     # с не допустимой длиной в названии
        'Яндекс книга лучшая книга для развития !!'
    ])
    def test_add_new_book_invalid_name_book_not_added(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)            # Добавляем название книги

        assert name not in collector.get_books_genre() # Проверяем, что книги не добавились
    
    @pytest.mark.parametrize('genre', [         # Применяем параметризацию для проверки добавления жанра
        'Фантастика',                           # добавляем каждый из 5 жанров заданных в self.genre
        'Ужасы',
        'Детективы',
        'Мультфильмы',
        'Комедии'
    ])
    def test_set_book_genre_valid_genre_genre_set(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Смешарики')  # Добавляем новую книгу

        collector.set_book_genre('Смешарики', genre) # Добавляем новой книге жанр

        assert collector.get_book_genre('Смешарики') == genre    # Проверяем добавленный жанр
    
    def test_get_book_genre_new_book_genre_is_empty(self):  # Проверка, что у добавленной книги нет жанра 
        collector = BooksCollector()

        collector.add_new_book('Незнайка на Луне')          # Добавили новую книгу

        assert collector.get_book_genre('Незнайка на Луне') == ''   # Проверили отсутствие жанра у добавленной книги
    
    def test_get_books_with_specific_genre_returns_correct_books(self):     # Проверка вывода списка книг по заданному жанру
        collector = BooksCollector()
        collector.add_new_book('Незнайка на Луне')          # Добавили новую книгу
        collector.add_new_book('Обитаемый остров')           # Добавили новую книгу
        collector.add_new_book('Вий')                       # Добавили новую книгу

        collector.set_book_genre('Незнайка на Луне', 'Фантастика')  # Добавили жанр
        collector.set_book_genre('Обитаемый остров', 'Фантастика')   # Добавили жанр
        collector.set_book_genre('Вий', 'Ужасы')                    # Добавили жанр

        result = collector.get_books_with_specific_genre('Фантастика')      # Вызывваем книги с жанром фантастика

        assert result == ['Незнайка на Луне', 'Обитаемый остров']            # Проверяем список книг с жанром фантастика
    
    @pytest.mark.parametrize('genre', [                                 # Параметризацией задаем 2 жанра с возрастным рейтингом
        'Ужасы',
        'Детективы'
    ])
    def test_get_books_for_children_age_rating_book_not_in_list(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Вий')                               # Добавили новую книгу
        collector.set_book_genre('Вий', genre)                      # Добавляем жанры не для детей, к новой книге

        assert 'Вий' not in collector.get_books_for_children()
    
    def test_add_book_in_favorites_book_added(self):                # Проверка добавления книги в избранное
        collector = BooksCollector()
        collector.add_new_book('Смешарики')                         # Добавляем книгу

        collector.add_book_in_favorites('Смешарики')                # Добавляем книгу в избранное

        assert 'Смешарики' in collector.get_list_of_favorites_books()   # Проверяем добавленную книгу в избранном
    
    def test_add_book_in_favorites_same_book_added_once(self):      # Проверка на повторное добавление гниги в избранное
        collector = BooksCollector()
        collector.add_new_book('Вий')                               # Добавили новую книгу

        collector.add_book_in_favorites('Вий')                      # Добавили книгу в избранное
        collector.add_book_in_favorites('Вий')                      # Повторно добавили книгу в избранное

        assert collector.get_list_of_favorites_books().count('Вий') == 1    # Проверили количество записей в избранной данной книги
    
    def test_delete_book_from_favorites_book_deleted(self):         # Проверка удаления книги из избранного
        collector = BooksCollector()
        collector.add_new_book('Капитанская дочка')                    # Добавили новую книгу
        collector.add_book_in_favorites('Капитанская дочка')           # Добавили книгу в избранное

        collector.delete_book_from_favorites('Капитанская дочка')       # Удаляем книгу из избранного

        assert 'Капитанская дочка' not in collector.get_list_of_favorites_books() # Проверяем есть ли книга в избранном
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()