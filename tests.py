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
    def test_set_book_genre_valid_genre_genre_set(self, genre): # Проверяем метод установки жанра
        collector = BooksCollector()
        
        collector.books_genre['Смешарики'] = ''  # Добавляем новую книгу

        collector.set_book_genre('Смешарики', genre) # Добавляем новой книге жанр

        assert collector.books_genre['Смешарики'] == genre    # Изменено: проверяем жанр книги

    
    def test_get_book_genre_returns_correct_genre(self):      # Проверка метода получения жанра кники по ее имени
        collector = BooksCollector()
        
        collector.books_genre['Незнайка на Луне'] = 'Фантастика'          # Добавили книгу Задали жанр

        result = collector.get_book_genre('Незнайка на Луне')

        assert result == 'Фантастика' # Проверили соответствие жанра по названию

                
    def test_add_new_book_genre_is_empty(self):  # Проверка, что у добавленной книги нет жанра 
        collector = BooksCollector()

        collector.add_new_book('Незнайка на Луне')         # Добавили новую книгу

        assert collector.books_genre['Незнайка на Луне'] == ''   # Проверили отсутствие жанра у добавленной книги
    
    
    def test_get_books_with_specific_genre_returns_correct_books(self):     # Проверка вывода списка книг по заданному жанру
        collector = BooksCollector()
        
        collector.books_genre = {                               # Добавили в словарь книг с жанрами
            'Незнайка на Луне': 'Фантастика',
            'Обитаемый остров': 'Фантастика',
            'Вий': 'Ужасы'
        }                    

        result = collector.get_books_with_specific_genre('Фантастика')      # Вызывваем книги с жанром фантастика

        assert result == ['Незнайка на Луне', 'Обитаемый остров']            # Проверяем список книг с жанром фантастика
    
    
    @pytest.mark.parametrize('genre', [                                 # Параметризацией задаем 2 жанра с возрастным рейтингом
        'Ужасы',
        'Детективы'
    ])
    def test_get_books_for_children_age_rating_book_not_in_list(self, genre):
        collector = BooksCollector()
        
        collector.books_genre['Вий'] = genre                      # Изменено: добавили словарь с книгой и жанрами не для детей

        result = collector.get_books_for_children()                # Передали в переменную список книг для детей

        assert 'Вий' not in result                                  # Проверили, что Вий не попал в список книг для детей
    
    
    def test_add_book_in_favorites_book_added(self):                # Проверка добавления книги в избранное
        collector = BooksCollector()
        
        collector.books_genre['Смешарики'] = 'Мультфильмы'                         # Добавляем книгу

        collector.add_book_in_favorites('Смешарики')                # Добавляем книгу в избранное

        assert 'Смешарики' in collector.favorites                  # Проверяем добавленную книгу в избранном
    
    
    def test_add_book_in_favorites_same_book_added_once(self):      # Проверка на повторное добавление книги в избранное
        collector = BooksCollector()
        collector.add_new_book('Вий')                               # Добавили новую книгу

        collector.add_book_in_favorites('Вий')                      # Добавили книгу в избранное
        collector.add_book_in_favorites('Вий')                      # Повторно добавили книгу в избранное

        assert collector.get_list_of_favorites_books().count('Вий') == 1    # Проверили количество записей в избранной данной книги
    
    
    def test_delete_book_from_favorites_book_deleted(self):         # Изменено: проверка удаления книги из избранного
        collector = BooksCollector()
        
        collector.favorites = ['Капитанская дочка']                  # Добавили новую книгу
        
        collector.delete_book_from_favorites('Капитанская дочка')       # Удаляем книгу из избранного

        assert 'Капитанская дочка' not in collector.favorites            # Проверяем есть ли книга в избранном
    
    
    def test_get_list_of_favorites_books_returns_favorites(self):       # Проверяем метод получения списка избранных книг
        collector = BooksCollector()

        expected_favorites = ['Смешарики', 'Капитанская дочка']         # Список книг добавили в переменную
        
        collector.favorites = expected_favorites                        # Добавили эти книги в список избранного

        result = collector.get_list_of_favorites_books()                # Вызвали список избранного и добавили в переменную

        assert result == expected_favorites                             # Проверили, что список книг в переменной result и expected_favorites одинаковый

    