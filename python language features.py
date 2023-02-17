from typing import List, Dict
import abc
import unittest


class Animal(abc.ABC):
    @abc.abstractmethod
    def __init__(self, age):
        self.age = age

    @abc.abstractmethod
    def get_description(self) -> str:
        pass


class Cat(Animal):
    def __init__(self, age):
        super().__init__(age)

    def get_description(self) -> str:
        return "Cat" + str(self.age)


class Dog(Animal):
    def __init__(self, age):
        super().__init__(age)

    def get_description(self) -> str:
        return "Dog" + str(self.age)


class AbstractClassTest(unittest.TestCase):

    def test_abstract_class_init(self):
        with self.assertRaises(TypeError):
            Animal(1)

    def test_concrete_class(self):
        self.assertEqual(Dog(1).get_description(), "Dog1")
        self.assertEqual(Cat(2).get_description(), "Cat2")


class Sort:
    @staticmethod
    def regular_sort(nums: List[int]):
        nums.sort()

        return nums

    @staticmethod
    def custom_sort_by_weight(nums: List[int], custom_order: Dict[int, int]):
        def get_sort_key(num):
            return custom_order[num]

        nums.sort(key=get_sort_key)
        # nums.sort(key=lambda num: custom_order[num])

        return nums

    @staticmethod
    def custom_sort_by_length(strings: List[str]):
        def get_sort_key(string):
            return len(string)

        strings.sort(key=get_sort_key)
        # strings.sort(key=lambda string: len(string))

        return strings


class TestSort(unittest.TestCase):
    def test_regular_sort(self):
        self.assertEqual(
            Sort.regular_sort([3, 1, 2]),
            [1, 2, 3]
        )
        self.assertEqual(
            Sort.custom_sort_by_length(["aaa", "bb", "a", "b", "c"]),
            ['a', 'b', 'c', 'bb', 'aaa']
        )

    def test_custom_sort_by_weight(self):
        custom_order = {1: 3, 2: 2, 3: 1}
        self.assertEqual(
            Sort.custom_sort_by_weight([3, 1, 2], custom_order),
            [3, 2, 1]
        )

    def test_custom_sort_by_length(self):
        self.assertEqual(
            Sort.custom_sort_by_length(["aaa", "bb", "a", "b", "c"]),
            ["a", "b", "c", "bb", "aaa"]
        )


unittest.main()
