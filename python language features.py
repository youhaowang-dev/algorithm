from dateutil import parser
from datetime import datetime
from typing import List, Dict
import abc
import unittest
import heapq


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


class Vals:  # ObjectWithCustomComparator
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    # override the <, __gt__ is the inverse
    def __lt__(self, other):
        if self.val1 == other.val1:
            return self.val2 < other.val2

        return self.val1 < other.val1

    def __repr__(self):
        return "val1: %d val2: %d" % (self.val1, self.val2)


class TestCustomComparator(unittest.TestCase):
    def test_sort(self):
        val1 = Vals(1, 2)
        val2 = Vals(1, 1)
        val3 = Vals(2, 0)
        vals = [val1, val2, val3]
        print(val1)
        print(val2)
        print(val3)
        vals.sort()
        self.assertEqual(vals, [val2, val1, val3])

    def test_heap(self):
        val1 = Vals(1, 2)
        val2 = Vals(1, 1)
        val3 = Vals(2, 0)
        min_heap = list()
        heapq.heappush(min_heap, val1)
        heapq.heappush(min_heap, val2)
        heapq.heappush(min_heap, val3)
        self.assertEqual(heapq.heappop(min_heap), val2)
        self.assertEqual(heapq.heappop(min_heap), val1)
        self.assertEqual(heapq.heappop(min_heap), val3)


class DataTime:
    def get_closest_k_days(days, target_day, k):
        min_heap = list()
        for day in days:
            # diff = abs(day.timestamp() - target_day.timestamp())
            diff = abs(day - target_day)  # datetime.timedelta
            heapq.heappush(min_heap, (-diff, day))  # max diff at peak
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        output = list()
        for _, day in min_heap:
            output.append(day)

        return output


class TestDataTime(unittest.TestCase):
    def test_closest(self):
        day1 = parser.parse('2022-12-21')
        day2 = parser.parse('2022-12-22')
        day3 = parser.parse('2022-12-23')
        day4 = parser.parse('2022-12-24')
        day5 = datetime(2022, 12, 25)
        day6 = datetime(2022, 12, 26)
        day7 = datetime(2022, 12, 27)
        day8 = datetime(2022, 12, 28)

        self.assertEqual(
            DataTime.get_closest_k_days(
                [day1, day2, day3, day4, day5, day6, day7, day8], day3, 3),
            [datetime(2022, 12, 22, 0, 0),
             datetime(2022, 12, 24, 0, 0),
             datetime(2022, 12, 23, 0, 0)]
        )
        self.assertEqual(
            DataTime.get_closest_k_days(
                [day1, day2, day3, day4, day5, day6, day7, day8], day3, 5),
            [datetime(2022, 12, 21, 0, 0),
             datetime(2022, 12, 25, 0, 0),
             datetime(2022, 12, 23, 0, 0),
             datetime(2022, 12, 24, 0, 0),
             datetime(2022, 12, 22, 0, 0)]
        )


unittest.main()
