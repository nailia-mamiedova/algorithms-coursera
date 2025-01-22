""" Given file IntegerArray.txt, which contains all the 100,000 integers
between 1 and 100,000 (inclusive) in some order, with no integer repeated.

Your task is to compute the number of inversions in the file given, where the ith row of the file indicates the
ith entry of an array.

Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.
The numeric answer for the given input file should be typed in the space below.
"""

def find_number_of_split_inversions(left_array, right_array) -> list:
    sorted_array = []
    split_inversions = 0

    i = j = 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            sorted_array.append(left_array[i])
            i += 1
        else:
            sorted_array.append(right_array[j])
            split_inversions += len(left_array) - i
            j += 1

    sorted_array.extend(left_array[i:])
    sorted_array.extend(right_array[j:])

    return [sorted_array, split_inversions]

def find_number_of_inversions(array: list) -> list:
    if len(array) == 1:
        return [array, 0]

    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    sorted_left, inversions_left = find_number_of_inversions(left)
    sorted_right, inversions_right = find_number_of_inversions(right)
    sorted_array, split_inversions = find_number_of_split_inversions(sorted_left, sorted_right)

    sum_of_inversions = inversions_left + inversions_right + split_inversions

    return [sorted_array, sum_of_inversions]


with open('IntegerArray.txt', 'r') as f:
    result, count = find_number_of_inversions([int(l) for l in f])
    print(f"Number of inversions in array: {count}")
