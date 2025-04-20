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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    def test_default_list_of_genres_is_true(self):
        collector = BooksCollector()
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']


    def test_add_new_book_adds_three_books(self):
        collector = BooksCollector()
        collector.add_new_book('Железный человек')
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Анекдоты категории Б')
        assert len(collector.get_books_genre()) == 3


    def test_set_book_genre_sets_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Железный человек')
        collector.set_book_genre('Железный человек','Фантастика')
        assert collector.get_books_genre() == {'Железный человек':'Фантастика'}


    def test_get_book_genre_returns_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Железный человек')
        assert collector.books_genre.get('Железный человек') == ''


    def test_get_books_with_specific_genre_returns_books_of_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Железный человек')
        collector.set_book_genre('Железный человек', 'Фантастика')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.add_new_book('Анекдоты категории Б')
        collector.set_book_genre('Анекдоты категории Б', 'Комедии')
        collector.add_new_book('Сказки для детей')
        collector.set_book_genre('Сказки для детей', 'Мультфильмы')
        collector.add_new_book('Как проснуться в 7:00 и не умереть')
        collector.set_book_genre('Как проснуться в 7:00 и не умереть', 'Фантастика')
        collector.get_books_with_specific_genre('Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Железный человек','Как проснуться в 7:00 и не умереть']


    def test_get_books_genre_returns_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Анекдоты категории Б')
        collector.set_book_genre('Анекдоты категории Б', 'Комедии')
        collector.add_new_book('Как проснуться в 7:00 и не умереть')
        collector.set_book_genre('Как проснуться в 7:00 и не умереть', 'Фантастика')
        assert collector.get_books_genre() == {'Анекдоты категории Б':'Комедии','Как проснуться в 7:00 и не умереть':'Фантастика'}

    @pytest.mark.parametrize('name,genre',[['Шерлок Холмс', 'Детективы'],['Сказки для детей', 'Мультфильмы'],['Кошмар на работе', 'Ужасы'],['Рон Уизли и Чемпионат по Квиддичу', 'Фантастика']])
    def test_get_books_for_children_returns_child_friendly_books(self,name,genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name,genre)
        books_for_children_genres=[]
        for name,genre in collector.books_genre.items():
            books_for_children_genres.append(genre)
            return books_for_children_genres
        assert all(genre not in books_for_children_genres for genre in collector.genre_age_rating)


    def test_add_book_in_favorites_adds_book_name(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.add_book_in_favorites('Шерлок Холмс')
        assert any(name in collector.get_list_of_favorites_books() for name in collector.get_books_genre())

    def test_delete_book_from_favorites_deletes_book_name(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.delete_book_from_favorites('Шерлок Холмс')
        assert any(name not in collector.get_list_of_favorites_books() for name in collector.get_books_genre())

    @pytest.mark.parametrize('name',['Шерлок Холмс','Рон Уизли и Чемпионат по Квиддичу'])
    def test_get_list_of_favorites_books_returns_favorites(self,name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.get_list_of_favorites_books()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.get_list_of_favorites_books()
        assert collector.favorites == [name]
