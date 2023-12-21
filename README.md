Объяснение того, какие сценарии покрыты тестами и почему вы выбрали именно эти сценарии:<br>
Тестирование функции get_average:<br>
Сценарии:<br>
Пустой список: Проверка, что функция возвращает 0 для пустого списка.
Непустой список: Проверка, что функция правильно вычисляет среднее значение для заданного списка.<br>
Почему выбраны:<br>
Эти сценарии проверяют базовую функциональность вычисления среднего значения списка.

Тестирование функции compare_averages:<br>
Сценарии:<br>
Равные средние значения: Проверка, что при равенстве средних значений списков возвращается соответствующее сообщение.
Первый список с большим средним: Проверка, что при большем среднем значении первого списка возвращается соответствующее сообщение.
Второй список с большим средним: Проверка, что при большем среднем значении второго списка возвращается соответствующее сообщение.<br>
Почему выбраны:<br>
Эти сценарии проверяют различные варианты сравнения средних значений двух списков.

Тестирование функции main:<br>
Сценарии:<br>
Возврат сообщения о сравнении средних значений: Проверка, что функция main возвращает правильное сообщение о сравнении средних значений.<br>
Почему выбран:<br>
Этот сценарий предоставляет дополнительное утверждение относительно корректной работы функции compare_averages.


![Coverage](images/coverage.png)

![Pylint with compare.py](images/pylint_with_compare.png)

![Pylint with test_compare.py](images/pylint_with_test_compare.png)
