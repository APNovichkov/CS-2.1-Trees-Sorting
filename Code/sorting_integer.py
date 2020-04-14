#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.

    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

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

    max_num = max(numbers)
    buckets = [[] for i in range(num_buckets)]

    for num in numbers:
        b_idx = _get_bucket_index(num, num_buckets, max_num)
        buckets[b_idx].append(num)
        buckets[b_idx].sort()

    number_index = 0
    for bucket in buckets:
        for num in bucket:
            numbers[number_index] = num
            number_index += 1

def _get_bucket_index(num, num_buckets, max_num):
    return (num * num_buckets) // (max_num + 1)


if __name__ == '__main__':
    # l1 = [1, 3, 4, 2, 4, 1, 10]
    # print(f'before: {l1}')
    # counting_sort(l1)
    # print(f'after: {l1}')

    l2 = [1, 3, 4, 2, 4, 1, 10, 41]
    print(f'before: {l2}')
    bucket_sort(l2)
    print(f'after: {l2}')
