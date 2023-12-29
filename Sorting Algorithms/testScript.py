from Class.sortingAlgorithms import SORT

# TODO: Convert to user entered list via HMI
testList = [9, 0, 4, 6, 2]

# Display the original list unsorted 
# TODO: convert the output to an HMI window rather than command line
sortedList = SORT(testList)
sortedList.showUnsortedList()