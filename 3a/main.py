import random
import time
import sys
sys.setrecursionlimit(2000000)


# DATA GENERATION

def generate_data(n):
    data = []
    for i in range(1, n + 1):
        data.append((i, f"Person{i}", random.randint(18, 80), random.uniform(30000.0, 500000.0)))
    return data



def test_case_1():
    """All identical - 1M records"""
    return [(i, f"Person{i}", 30, 50000.0) for i in range(1, 1000001)]


def test_case_2():
    """Sequential duplicates - 1M in 5 groups"""
    data = []
    for i in range(1, 200001):
        data.append((i, f"Person{i}", 25, 50000.0))
    for i in range(200001, 400001):
        data.append((i, f"Person{i}", 30, 60000.0))
    for i in range(400001, 600001):
        data.append((i, f"Person{i}", 35, 70000.0))
    for i in range(600001, 800001):
        data.append((i, f"Person{i}", 40, 80000.0))
    for i in range(800001, 1000001):
        data.append((i, f"Person{i}", 45, 90000.0))
    return data


def test_case_3():
    """Interleaved duplicates - 1M alternating"""
    data = []
    for i in range(1, 1000001):
        if i % 2 == 0:
            data.append((i, f"Person{i}", 30, 50000.0))
        else:
            data.append((i, f"Person{i}", 40, 60000.0))
    return data


def test_case_4():
    """High duplicate density - 1M records, 6 keys"""
    data = []
    ages = [25, 30, 35]
    salaries = [50000.0, 60000.0]
    for i in range(1, 1000001):
        data.append((i, f"Person{i}", ages[i % len(ages)], salaries[i % len(salaries)]))
    return data


def test_case_5():
    """Mixed - 1M records (80% unique + 20% duplicates)"""
    data = []
    
    for i in range(1, 800001):
        age = 18 + (i % 63)
        salary = 30000.0 + (i * 0.5)
        data.append((i, f"Person{i}", age, salary))
    
    for i in range(800001, 900001):
        data.append((i, f"Person{i}", 30, 50000.0))
    for i in range(900001, 1000001):
        data.append((i, f"Person{i}", 35, 60000.0))
    
    return data


# SORTING ALGORITHMS

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if compare_tuples(left[i], right[j]) <= 0:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        lt, gt = partition_3way(arr, low, high)
        quick_sort(arr, low, lt - 1)
        quick_sort(arr, gt + 1, high)
    
    return arr


def partition_3way(arr, low, high):
    
    rand_idx = random.randint(low, high)
    arr[low], arr[rand_idx] = arr[rand_idx], arr[low]
    
    pivot = arr[low]
    lt = low
    gt = high
    i = low + 1
    
    while i <= gt:
        cmp = compare_tuples(arr[i], pivot)
        if cmp < 0:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif cmp > 0:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    
    return lt, gt


def compare_tuples(tuple1, tuple2):
    if tuple1[2] < tuple2[2]:
        return -1
    elif tuple1[2] > tuple2[2]:
        return 1
    if tuple1[3] < tuple2[3]:
        return -1
    elif tuple1[3] > tuple2[3]:
        return 1
    return 0


# MAIN

def main():
    test_cases = {
        1: test_case_1, 2: test_case_2, 3: test_case_3, 
        4: test_case_4, 5: test_case_5
    }
    
    if len(sys.argv) > 1 and sys.argv[1].startswith('test'):
        try:
            test_num = int(sys.argv[1].replace('test', ''))
            if test_num not in test_cases:
                print(f"Invalid test case: {test_num} (use test1-test5)")
                return
            
            data = test_cases[test_num]()
            print(f"Test Case {test_num}: {len(data)} records")
            
        except ValueError:
            print("Usage: python main.py test[1-5]")
            return
    else:
        if len(sys.argv) > 1:
            try:
                N = int(sys.argv[1])
            except ValueError:
                print("Usage: python main.py [size] or python main.py test[1-5]")
                return
        else:
            user_input = input("Dataset size (default 1000000): ").strip()
            N = int(user_input) if user_input else 1000000
        
        data = generate_data(N)
        print(f"Dataset: {N:,} records")
    
    start = time.time()
    merge_result = merge_sort(data.copy())
    merge_time = time.time() - start
    print(f"Merge: {merge_time:.4f}s")
    
    start = time.time()
    quick_result = quick_sort(data.copy())
    quick_time = time.time() - start
    print(f"Quick: {quick_time:.4f}s")
    
    print(f"\nFirst 10 IDs (Merge): {[r[0] for r in merge_result[:10]]}")
    print(f"First 10 IDs (Quick): {[r[0] for r in quick_result[:10]]}")


if __name__ == "__main__":
    main()