from abc import ABC, abstractmethod
import copy

class StrategySorter(ABC):
    @abstractmethod
    def sort(self, list):
        pass

class BubleSort(StrategySorter):
    def sort(self, list: list):
        n = len(list)
        for x in range(n):
            for y in range(0, n-x-1):
                if list[y] > list[y+1]:
                    list[y], list[y+1] = list[y+1], list[y]

class SelectionSort(StrategySorter):
    def sort(self, list):
        for x in range(len(list)):
            min_index = x
            for y in range(x + 1, len(list)):
                if list[y] < list[min_index]:
                    min_index = y
            list[x], list[min_index] = list[min_index], list[x]


class InsertionSort(StrategySorter):
    def sort(self, list):
        for x in range(1, len(list)):
            key = list[x]
            y = x - 1
            while y >= 0 and list[y] > key:
                list[y+1] = list[y]
                y -= 1
            list[y + 1] = key

class Context():
    def __init__(self, strategy: StrategySorter):
        self._stategy = strategy

    def set_sort(self, strategy: StrategySorter):
        self._stategy = strategy

    def make_sort(self, array: list):
        copy_list = copy.copy(array)
        self._stategy.sort(copy_list)
        return copy_list



if __name__ == "__main__":
    example_list = [1, 2, 5, 18, 3, 13, 255, 63, 10, 23, 46]

    context = Context(BubleSort())
    print("По замовченню стоїть бабл")
    print(f"Список до - {example_list} і список після - {context.make_sort(example_list)}")


    context.set_sort(SelectionSort())
    print("Тепер стоїть Селекшн")
    print(f"Список до - {example_list} і список після - {context.make_sort(example_list)}")


    context.set_sort(InsertionSort())
    print("Тепер стоїть Інсерт")
    print(f"Список до - {example_list} і список після - {context.make_sort(example_list)}")

