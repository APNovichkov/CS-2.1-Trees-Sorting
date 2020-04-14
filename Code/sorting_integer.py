#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list

    max_num = max(numbers)
    min_num = min(numbers)
    c_arr = [0] * (max_num - min_num + 1)

    for num in numbers:
        c_arr[num - min_num] += 1

    numbers_index = 0
    for index, counts in enumerate(c_arr):
        val = index + min_num
        for i in range(0, counts):
            numbers[numbers_index] = val
            numbers_index += 1


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


if __name__ == '__main__':
    l1 = [1, 3, 4, 2, 4, 1, 10]
    print(f'before: {l1}')
    counting_sort(l1)
    print(f'after: {l1}')
