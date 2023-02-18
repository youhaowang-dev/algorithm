from typing import List, Dict
import abc
import unittest


class Animal(abc.ABC):
    # abstractmethod means cannot init object if child does not override all the abstractmethod
    @abc.abstractmethod
    def __init__(self, age: int, name: str):
        self.age = age
        self.name = name

    @abc.abstractmethod
    def get_description(self) -> str:
        pass

    def get_name(self) -> str:
        return self.name


class Cat(Animal):
    def __init__(self, age: int, name: str):
        super().__init__(age, name)

    def get_description(self) -> str:
        return "Cat" + str(self.age) + self.get_name()


class Dog(Animal):
    def __init__(self, age: int, name: str):
        super().__init__(age, name)

    def get_description(self) -> str:
        return "Dog" + str(self.age) + self.get_name()


class Bird(Animal):
    NAME_SUFFIX = "#"

    def __init__(self, age: int, name: str):
        super().__init__(age, name)

    def get_description(self) -> str:
        return "Bird" + str(self.age) + self.get_name()

    def get_name(self) -> str:
        return super().get_name() + self.NAME_SUFFIX


class AbstractClassTest(unittest.TestCase):

    def test_abstract_class_init(self):
        with self.assertRaises(TypeError):
            Animal(1)

    def test_concrete_class(self):
        self.assertEqual(Dog(1, 'lily').get_description(), "Dog1lily")
        self.assertEqual(Cat(2, 'mark').get_description(), "Cat2mark")
        self.assertEqual(Bird(2, 'bob').get_description(),
                         "Bird2bob"+Bird.NAME_SUFFIX)


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


class ListDict(unittest.TestCase):
    def test_pop_by_key(self):
        nums = [1, 2, 3]
        nums.pop(1)
        self.assertEqual(nums, [1, 3])
        num_to_val = {num: num for num in nums}  # dict comprehension
        self.assertEqual(num_to_val, {1: 1, 3: 3})
        num_to_val.pop(1)
        self.assertEqual(num_to_val, {3: 3})


unittest.main()
