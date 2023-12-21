import pytest

from compare import CompareLists, main


class TestCompareLists:
    """Класс для тестирования CompareLists."""
    @pytest.fixture
    def compare_lists_instance(self):
        """Фикстура с экземпляром класса CompareLists."""
        first_list = [1, 2, 3, 4, 5]
        second_list = [6, 7, 8, 9, 10]
        return CompareLists(first_list, second_list)

    @pytest.mark.parametrize(
        "a, expected", [([], 0), ([1, 2, 3, 4, 5], 3)]
    )
    def test_get_average(self, a, expected):
        """Тестирование функции get_average."""
        assert CompareLists.get_average(a) == expected

    def test_compare_averages_equal(self, compare_lists_instance):
        """Тестирование функции compare_averages при условии равенства списков."""
        compare_lists_instance.second_list = [1, 2, 3, 4, 5]
        result = compare_lists_instance.compare_averages()
        assert result == 'Средние значения равны'

    def test_compare_averages_first_greater(self, compare_lists_instance):
        """Тестирование функции compare_averages при условии,
        что первый список имеет большее среднее значение.
        """
        compare_lists_instance.first_list = [11, 12, 13, 14, 15]
        result = compare_lists_instance.compare_averages()
        assert result == 'Первый список имеет большее среднее значение'

    def test_compare_averages_second_greater(self, compare_lists_instance):
        """Тестирование функции compare_averages при условии,
        что второй список имеет большее среднее значение.
        """
        result = compare_lists_instance.compare_averages()
        assert result == 'Второй список имеет большее среднее значение'


def test_main():
    """Тестирование функции main."""
    assert main() == 'Второй список имеет большее среднее значение'
