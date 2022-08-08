import unittest
from parameterized import parameterized
from task1_accounting import find_doc, find_shelf, people, shelf, add


class TestFunctiuns(unittest.TestCase):

    @parameterized.expand(
        [
            ("11-2", 1),
            ("11-3", None)
        ]
    )
    def test_find_doc(self, num, result):
        c_result = find_doc(num)
        self.assertEqual(c_result, result)

    @parameterized.expand(
        [
            ("11-2", '1'),
            ("11-3", None)
        ]
    )
    def test_find_shelf(self, num, result):
        c_result = find_shelf(num)
        self.assertEqual(c_result, result)

    @parameterized.expand(
        [
            ("11-2", 'Геннадий Покемонов'),
            ("11-3", 'Документа с номером 11-3 нет.')
        ]
    )
    def test_people(self, num, result):
        c_result = people(num)
        self.assertEqual(c_result, result)

    @parameterized.expand(
        [
            ("11-2", '1'),
            ("11-3", 'Документ с номером 11-3 не найден на полках.')
        ]
    )
    def test_shelf(self, num, result):
        c_result = shelf(num)
        self.assertEqual(c_result, result)

    @parameterized.expand(
        [
            ("passport", "11-2", 'Иванов Иван', "1", "Документ с номером 11-2 уже есть в базе."),
            ("passport", "22-2", 'Иванов Иван', "4", "Нет полки с номером 4. Документ не добавлен."),
            ("passport", "22-2", 'Иванов Иван', "3", "Документ с номером 22-2 добавлен. Помещен на полку 3.")
        ]
    )
    def test_add(self, itype, inum, iname, ishelf, result):
        c_result = add(itype, inum, iname, ishelf)
        self.assertEqual(c_result, result)
