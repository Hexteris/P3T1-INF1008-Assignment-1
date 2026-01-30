import random, time

def merge(left, right):
    '''Merges two sorted lists of tuples based on the value at index [1].'''
    result = []
    i = j = 0

    # Compare values from both halves.
    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from either list.
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(arr):
    '''Recursively splits and merges a list of tuples using Merge Sort.'''
    if len(arr) <= 1: return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def bucket_sort(arr):
    '''Sorts a list of tuples in-place using Bucket Sort.'''
    if not arr: return arr

    n = len(arr)

    # Find the range of values for normalization.
    min_val = max_val = arr[0][1]
    for i in range(1, len(arr)):
        val = arr[i][1]
        if val < min_val: min_val = val
        elif val > max_val: max_val = val

    if min_val == max_val:
        return arr

    range_val = max_val - min_val

    # Create n empty buckets.
    buckets = [[] for _ in range(n)]

    # Normalize and place into buckets.
    for item in arr:
        # Map the value to a bucket index from 0 to (n - 1).
        idx = int((item[1] - min_val) / range_val * (n - 1))
        buckets[idx].append(item)

    # Sort each bucket and overwrite the original array.
    # The list comprehension runs merge_sort on each bucket and flattens them.
    arr[:] = [item for bucket in buckets for item in merge_sort(bucket)]

def is_stable(arr):
    '''Checks if the sort was stable by verifying if duplicate values maintained their original order.'''
    for i in range(len(arr) - 1):
        if arr[i][1] == arr[i + 1][1] and arr[i][0] > arr[i + 1][0]:
            return False
    return True

def log(case, result, elapsed, stable):
    '''Writes the result of a test case to an output file.'''
    case_name = test_cases[case]['name']
    case_arr = test_cases[case]['arr'].copy()

    with open('Q3b_output.txt', 'w') as f:
        f.write(f'===== Bucket Sort on {case_name} =====\n')
        f.write(f'Time Elapsed: {elapsed:.2f} ms | Stable: {stable}\n\n')

        header1 = f'Before Sorting ({len(case_arr):,})'
        header2 = f'Result ({len(case_arr):,})'
        f.write(f'{header1:<{30}} |\t{header2}\n')
        f.write('-' * 60 + '\n')

        for i in range(len(case_arr)):
            f.write(f'{str(case_arr[i]):<{30}} |\t{str(result[i])}\n')

def run(case):
    '''Executes a test case, measures performance, and triggers logging.'''
    case_name = test_cases[case]['name']
    case_arr = test_cases[case]['arr'].copy()

    print(f'\n===== Bucket Sort on {case_name} =====\n')
    print(f'Before Sorting ({len(case_arr):,}):\n{case_arr[:10]}, [...], {case_arr[-10:]}\n')

    start_time = time.perf_counter()
    bucket_sort(case_arr)
    end_time = time.perf_counter()

    elapsed = (end_time - start_time) * 1000
    stable = is_stable(case_arr)

    print(f'Result ({len(case_arr):,}):\n{case_arr[:10]}, [...], {case_arr[-10:]}\n')
    print(f'Time Elapsed: {elapsed:.2f} ms | Stable: {stable}\n')

    print('Saving full output to file...')
    log(case, case_arr, elapsed, stable)
    print('View full output at Q3b_output.txt')

#
# Program start
#
while True:
    try:
        records = int(input('\nEnter number of records to generate (1 - 1,000,000): '))
        if 1 <= records <= 1000000:
            break
        print('Invalid input.')
    except:
        print('Invalid input.')

print('\nInitializing...')

#
# Generate records and test cases.
#
base_data = [(i, i) for i in range(records)]

unsorted_data = base_data.copy()
random.shuffle(unsorted_data)

reversed_data = base_data[::-1]
identical_data = [(i, 67) for i in range(records)]
few_unique_data = [(i, random.choice([10, 20, 30, 40, 50])) for i in range(records)]
floating_point_data = [(i, random.uniform(1, records)) for i in range(records)]
negative_data = [(i * -1, i * -1) for i in range(records)]
empty_data = []

nearly_sorted_data = base_data.copy()
for _ in range(1000):
    idx1, idx2 = random.randint(0, records - 1), random.randint(0, records - 1)
    nearly_sorted_data[idx1], nearly_sorted_data[idx2] = nearly_sorted_data[idx2], nearly_sorted_data[idx1]

test_cases = [
    {'name': 'Unsorted Data', 'arr': unsorted_data},
    {'name': 'Reversed Data', 'arr': reversed_data},
    {'name': 'Identical Data', 'arr': identical_data},
    {'name': 'Few Unique Data', 'arr': few_unique_data},
    {'name': 'Nearly Sorted Data', 'arr': nearly_sorted_data},
    {'name': 'Floating Point Data', 'arr': floating_point_data},
    {'name': 'Negative Data', 'arr': negative_data},
    {'name': 'Empty Data', 'arr': empty_data}
]

print(f'Generated {records:,} records and {len(test_cases)} test cases.')

#
# REPL
#
while True:
    print('\n===== TEST CASES =====')
    for i in range(len(test_cases)):
        print(f'{i + 1}. {test_cases[i]['name']}')

    try:
        case = int(input('\nEnter test case: '))
        if 1 <= case <= len(test_cases):
            run(case - 1)
        else:
            print('Invalid option.')
    except:
        print('Invalid option.')