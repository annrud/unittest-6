class CompareLists:
    """Класс для сравнения двух списков."""

    def __init__(self, first_list, second_list):
        self.first_list = first_list
        self.second_list = second_list

    @staticmethod
    def get_average(some_list):
        """Получение среднего значения списка."""
        if not some_list:
            return 0
        return sum(some_list) / len(some_list)

    def compare_averages(self) -> object:
        """Сравнение двух списков через среднее значение."""
        first_average = self.get_average(self.first_list)
        second_average = self.get_average(self.second_list)
        if first_average == second_average:
            return 'Средние значения равны'
        if first_average > second_average:
            return 'Первый список имеет большее среднее значение'
        return 'Второй список имеет большее среднее значение'


def main():
    """Проверка работы CompareLists."""
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]

    compare_lists = CompareLists(list1, list2)
    result = compare_lists.compare_averages()

    return result


if __name__ == "__main__":
    print(main())
