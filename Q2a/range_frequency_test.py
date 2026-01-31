import time
import random
import bisect

def test_sorting_only():
    """Test only the sorting part to verify O(n log n)"""
    
    sizes = [10000, 20000, 40000, 80000, 160000]
    
    print("Testing SORTING ONLY (to verify O(n log n))")
    print("-" * 60)
    print(f"{'Size':<10} {'Time (s)':<12} {'Ratio':<10} {'Expected':<10}")
    print("-" * 60)
    
    prev_time = None
    
    for size in sizes:
        index_map = {}
        for i in range(size):
            val = i  # All distinct values
            if val not in index_map:
                index_map[val] = []
            index_map[val].append(i)
        
        start = time.perf_counter()
        for val in index_map:
            index_map[val].sort()  
        elapsed = time.perf_counter() - start
        
        if prev_time is not None:
            ratio = elapsed / prev_time
            expected = 2.15  # When doubling size, O(n log n) ratio is ~2.15x
            status = "✓" if 1.8 <= ratio <= 2.4 else "✗"
            print(f"{size:<10} {elapsed:.6f}    {ratio:.3f}x     {expected:.3f}x   {status}")
        else:
            print(f"{size:<10} {elapsed:.6f}    -          -         -")
        
        prev_time = elapsed

test_sorting_only()