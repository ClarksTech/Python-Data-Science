class SORT:
    """Sort class implements the following different sorting algorithms to return the list in ascending order:

    - Bubble Sort
    - Selection Sort
    - Insertion Sort
    - Shell Sort
    - Heap Sort
    - Merge Sort
    - Quick Sort
    - Counting Sort

    Attributes:
        list: An unordered integer list 
    """

    def __init__(self):
        """Initializes the instance with an empty list.
        """
        self.list = []

    def showList(self, list: list):
        """Prints the list
        """
        self.list = list
        print("List is: " + str(self.list))

    def bubbleSort(self, list: list):
        """Performs bubble sort in place on the unsorted list.

        :param list: Initially an unsorted list
        :return: No return as list is sorted in place meaning original list variable now holds the sorted list

        :Space Complexity: O(1)
        :Time Complexity: O(n^2)
        """
        self.list = list
        unordered = False
        for el in range(len(self.list)-1):
            for el_ in range(len(self.list)-el-1):
                if self.list[el_] > self.list[el_+1]:
                    self.list[el_], self.list[el_+1] = self.list[el_+1], self.list[el_]
                    unordered = True
                if not unordered:
                    return

    def selectionSort(self, list: list):
        """Performs selection sort in place on unsorted list.

        :param list: Initially an unsorted list
        :return: No return as list is sorted in place meaning original list variable now holds the sorted list

        :Space Complexity: O(1)
        :Time Complexity: O(n^2)
        """
        self.list = list
        for el in range(len(self.list)):
            minEl = el
            for el_ in range(minEl+1, len(self.list)):
                if self.list[el_] < self.list[minEl]:
                    minEl = el_
            self.list[el], self.list[minEl] = self.list[minEl], self.list[el]
        return

    def insertionSort(self, list: list):
        """Performs insertion sort on unsorted list.

        :param list: Initially an unsorted list
        :return: No return as list is sorted in place meaning original list variable now holds the sorted list

        :Space Complexity: O(1)
        :Time Complexity: O(n^2)
        """
        self.list = list
        for el in range(1, len(self.list)):
            sortedEl = self.list[el]
            el_ = el - 1
            while self.list[el_] > sortedEl and el_ >= 0:
                self.list[el_ + 1] = self.list[el_]
                el_ -= 1
            self.list[el_ + 1] = sortedEl
        return    

    def shellSort(self):
        """Performs shell sort on unsorted list.
        """

    def heapSort(self):
        """Performs heap sort on unsorted list.
        """

    def mergeSort(self):
        """Performs merge sort on unsorted list.
        """

    def quickSort(self):
        """Performs quick sort on unsorted list.
        """

    def countingSort(self):
        """Performs counting sort on unsorted list.
        """

