"""
Range Frequency Query - O(n log n) algorithm
"""

import bisect
from typing import List, Tuple, Dict
import sys

class RangeFrequencyQuery:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.index_map: Dict[int, List[int]] = {}
        
        # Build index map: O(n)
        for i, val in enumerate(arr):
            if val not in self.index_map:
                self.index_map[val] = []
            self.index_map[val].append(i)
        
        # Sort all index lists: O(n log n) total
        for val in self.index_map:
            self.index_map[val].sort()
    
    def query(self, left: int, right: int, value: int) -> int:
      
        # Value not in array: O(1)
        if value not in self.index_map:
            return 0
        
        indices = self.index_map[value]
        
        # Binary search for left boundary: O(log m)
        left_pos = bisect.bisect_left(indices, left)
        
        # Binary search for right boundary: O(log m)
        right_pos = bisect.bisect_right(indices, right) - 1
        
        # Check if range is valid
        if left_pos > right_pos:
            return 0
        
        return right_pos - left_pos + 1
    
    def batch_query(self, queries: List[Tuple[int, int, int]]) -> List[int]:
        return [self.query(left, right, value) for left, right, value in queries]

def test_range_frequency():
    print("=" * 60)
    print("RANGE FREQUENCY QUERY TEST SUITE")
    print("=" * 60)
    
    all_passed = True
    test_cases = []
    
    # Test Case 1: Basic functionality
    print("\nTest 1: Basic functionality")
    arr1 = [1, 2, 1, 3, 1]
    rfq1 = RangeFrequencyQuery(arr1)
    result1 = rfq1.query(0, 4, 1)
    expected1 = 3
    test_cases.append(("Basic", arr1, (0, 4, 1), result1, expected1))
    if result1 == expected1:
        print(f"✓ PASS: arr={arr1}, query(0,4,1)={result1}")
    else:
        print(f"✗ FAIL: Expected {expected1}, got {result1}")
        all_passed = False
    
    # Test Case 2: Value not in array
    print("\nTest 2: Value not in array")
    result2 = rfq1.query(0, 2, 5)
    expected2 = 0
    test_cases.append(("No value", arr1, (0, 2, 5), result2, expected2))
    if result2 == expected2:
        print(f"✓ PASS: query(0,2,5)={result2}")
    else:
        print(f"✗ FAIL: Expected {expected2}, got {result2}")
        all_passed = False
    
    # Test Case 3: Single element range
    print("\nTest 3: Single element range")
    arr3 = [5, 5, 5, 1, 1]
    rfq3 = RangeFrequencyQuery(arr3)
    result3 = rfq3.query(1, 1, 5)
    expected3 = 1
    test_cases.append(("Single element", arr3, (1, 1, 5), result3, expected3))
    if result3 == expected3:
        print(f"✓ PASS: arr={arr3}, query(1,1,5)={result3}")
    else:
        print(f"✗ FAIL: Expected {expected3}, got {result3}")
        all_passed = False
    
    # Test Case 4: Multiple queries
    print("\nTest 4: Multiple queries (batch)")
    arr4 = [1, 2, 1, 3, 1, 2, 1]
    rfq4 = RangeFrequencyQuery(arr4)
    queries4 = [(0, 4, 1), (2, 6, 2), (0, 6, 3)]
    results4 = rfq4.batch_query(queries4)
    expected4 = [3, 1, 1]
    test_cases.append(("Multiple queries", arr4, queries4, results4, expected4))
    if results4 == expected4:
        print(f"✓ PASS: queries={queries4}, results={results4}")
    else:
        print(f"✗ FAIL: Expected {expected4}, got {results4}")
        all_passed = False
    
    # Test Case 5: All identical elements
    print("\nTest 5: All identical elements")
    arr5 = [7, 7, 7, 7]
    rfq5 = RangeFrequencyQuery(arr5)
    result5 = rfq5.query(0, 3, 7)
    expected5 = 4
    test_cases.append(("All identical", arr5, (0, 3, 7), result5, expected5))
    if result5 == expected5:
        print(f"✓ PASS: arr={arr5}, query(0,3,7)={result5}")
    else:
        print(f"✗ FAIL: Expected {expected5}, got {result5}")
        all_passed = False
    
    # Test Case 6: Empty range
    print("\nTest 6: Empty range (left > right)")
    arr6 = [1, 2, 3, 4, 5]
    rfq6 = RangeFrequencyQuery(arr6)
    result6 = rfq6.query(3, 2, 3)
    expected6 = 0
    test_cases.append(("Empty range", arr6, (3, 2, 3), result6, expected6))
    if result6 == expected6:
        print(f"✓ PASS: query(3,2,3)={result6}")
    else:
        print(f"✗ FAIL: Expected {expected6}, got {result6}")
        all_passed = False
    
    # Test Case 7: Large array test (performance)
    print("\nTest 7: Large array performance test")
    arr7 = list(range(10000)) + [42] * 100  # 10,100 elements
    rfq7 = RangeFrequencyQuery(arr7)
    
    import time
    start = time.time()
    for _ in range(1000):
        rfq7.query(5000, 9000, 42)
    elapsed = time.time() - start
    
    # Should complete quickly (demonstrates O(log n) queries)
    if elapsed < 0.1:  # Less than 100ms for 1000 queries
        print(f"✓ PASS: 1000 queries on 10k array in {elapsed:.3f}s (< 0.1s)")
        performance_ok = True
    else:
        print(f"⚠ WARNING: Slow performance: {elapsed:.3f}s")
        performance_ok = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("ALL RANGE FREQUENCY TESTS PASSED ✓")
    else:
        print("SOME TESTS FAILED ✗")
    
    # Summary table
    print("\nTest Summary:")
    print("-" * 60)
    print(f"{'Test':<20} {'Result':<10} {'Expected':<10} {'Status':<10}")
    print("-" * 60)
    for name, arr, query, result, expected in test_cases:
        status = "PASS" if result == expected else "FAIL"
        if isinstance(query, tuple):
            q_str = f"{query[0]},{query[1]},{query[2]}"
        else:
            q_str = "multiple"
        print(f"{name:<20} {str(result):<10} {str(expected):<10} {status:<10}")
    
    return all_passed and performance_ok

def main():
    """Main function for standalone execution."""
    print("Range Frequency Query - O(n log n) Algorithm")
    print("=" * 50)
    
    # Interactive mode or test mode
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        test_range_frequency()
        return
    
    print("Enter array elements (space-separated integers):")
    arr_input = input().strip()
    if not arr_input:
        print("Running test suite...")
        test_range_frequency()
        return
    
    arr = list(map(int, arr_input.split()))
    rfq = RangeFrequencyQuery(arr)
    
    print(f"\nArray of size {len(arr)} preprocessed in O(n log n) time.")
    print("Enter queries as 'left right value' (one per line, empty to finish):")
    
    results = []
    while True:
        query_input = input().strip()
        if not query_input:
            break
        try:
            left, right, value = map(int, query_input.split())
            if left < 0 or right >= len(arr) or left > right:
                print("Error: Invalid range")
                continue
            result = rfq.query(left, right, value)
            results.append(result)
            print(f"  Result: {result}")
        except ValueError:
            print("Error: Invalid input format")
    
    if results:
        print(f"\nAll results: {results}")

if __name__ == "__main__":
    main()