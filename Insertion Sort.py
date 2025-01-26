# Insertion Sort
# Michael Perlin

# Start with some pre-determined array
arr = [13, 17, 18, 19, 2, 3, 6, 23, 47, 51]

# Insertion sort function, iteratively inserts numbers into correct position
# Essentially splits numbers into array into two groups, those being the sorted numbers and unsorted numbers, on each successive iteration
# when a new number is added to the sorted numbers group, algorithm compares numbers and rearranges numbers accordingly
def InsertionSort (arr):
    for i in range (1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key

# Function which monitors sorting progress and prints it out to the terminal
def SortProgress(arr):
    for i in range (1, len(arr)):
        CurrentArr = arr[:i + 1]
        InsertionSort(CurrentArr)
        print("Partially sorted:" , "," .join(map(str, CurrentArr)))

# Last function that prints the sorted array in a neat, comma-separated format.
def PrintArray (arr):
    print("Sorted array:","," .join(map(str, arr)))
if __name__ == "__main__":
    SortProgress(arr)
    InsertionSort(arr)
    PrintArray(arr)