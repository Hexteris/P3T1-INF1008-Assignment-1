"""
Graph 2-Coloring Problem - O(2^n) Exponential Algorithm
Demonstrates exponential time complexity through exhaustive backtracking.
"""

from typing import List, Tuple
import time
import sys

class Graph2ColoringSolver:
   
    
    def __init__(self, edges: List[Tuple[int, int]], num_vertices: int):
   
        if num_vertices <= 0:
            raise ValueError("Number of vertices must be positive")
        
        self.num_vertices = num_vertices
        self.edges = edges
        self.adj_list = [[] for _ in range(num_vertices)]
        
        for u, v in edges:
            if u < 0 or u >= num_vertices or v < 0 or v >= num_vertices:
                raise ValueError(f"Invalid edge ({u}, {v})")
            if u == v:
                raise ValueError(f"Self-loop at vertex {u}")
            
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
        
        self.solutions = []
        self.call_count = 0
    
    def solve(self) -> List[List[int]]:
        self.solutions = []
        self.call_count = 0
        
        coloring = [-1] * self.num_vertices
        self._backtrack(0, coloring)
        
        return self.solutions
    
    def _backtrack(self, vertex: int, coloring: List[int]) -> None:
        """
        Binary decision tree: each vertex colored 0 or 1.
        
        Creates 2 branches per vertex → 2^n total calls.
        """
        self.call_count += 1
        
        # Base: all vertices colored
        if vertex == self.num_vertices:
            if self._is_valid(coloring):
                self.solutions.append(coloring.copy())
            return
        
        # Try color 0
        coloring[vertex] = 0
        self._backtrack(vertex + 1, coloring)
        
        # Try color 1
        coloring[vertex] = 1
        self._backtrack(vertex + 1, coloring)
        
        coloring[vertex] = -1
    
    def _is_valid(self, coloring: List[int]) -> bool:
        """Check no adjacent vertices have same color."""
        for u in range(self.num_vertices):
            for v in self.adj_list[u]:
                if coloring[u] == coloring[v]:
                    return False
        return True


def demonstrate_exponential_growth():
    print("=" * 70)
    print("O(2^n) EXPONENTIAL GROWTH DEMONSTRATION")
    print("=" * 70)
    print(f"\n{'n':>3} | {'Calls':>12} | {'2^n':>12} | {'Time':>8}")
    print("-" * 70)
    
    results = []
    
    for n in range(4, 25, 2):
        edges = [(i, i+1) for i in range(n-1)]  # Path graph
        solver = Graph2ColoringSolver(edges, n)
        
        start = time.time()
        solver.solve()
        elapsed = time.time() - start
        
        results.append((n, solver.call_count, elapsed))
        print(f"{n:3d} | {solver.call_count:12,d} | {2**n:12,d} | {elapsed:8.4f}s")
        
        if elapsed > 3.0:
            print("\n⚠️  Exponential explosion - stopping at n=" + str(n))
            break
    
    # Growth ratios
    print("\n" + "=" * 70)
    print("DOUBLING PATTERN VERIFICATION")
    print("=" * 70)
    print(f"{'Transition':>12} | {'Call Ratio':>12} | {'Expected':>12}")
    print("-" * 70)
    
    for i in range(1, len(results)):
        n_prev, calls_prev, _ = results[i-1]
        n_curr, calls_curr, _ = results[i]
        
        ratio = calls_curr / calls_prev
        expected = 2 ** (n_curr - n_prev)
        
        print(f"n={n_prev:2d} → {n_curr:2d} | ×{ratio:11.2f} | ×{expected:11.1f}")


def test_graph_2_coloring():
    """Essential test cases."""
    print("\n" + "=" * 70)
    print("TEST SUITE")
    print("=" * 70)
    
    tests = [
        ("Path (bipartite)", [(0,1), (1,2), (2,3)], 4, True),
        ("Triangle (odd cycle)", [(0,1), (1,2), (2,0)], 3, False),
        ("Square (even cycle)", [(0,1), (1,2), (2,3), (3,0)], 4, True),
        ("Single vertex", [], 1, True),
        ("Star graph", [(0,1), (0,2), (0,3)], 4, True),
    ]
    all_passed = True
    
    for i, (name, edges, n, should_have_solutions) in enumerate(tests, 1):
        print(f"\n[Test {i}] {name}")
        try:
            solver = Graph2ColoringSolver(edges, n)
            solutions = solver.solve()
            has_solutions = len(solutions) > 0
            
            if has_solutions == should_have_solutions:
                print(f"  ✓ PASS: {len(solutions)} solution(s), {solver.call_count} calls")
                if solutions and len(solutions) <= 3:
                    for sol in solutions:
                        print(f"    {sol}")
            else:
                print(f"  ✗ FAIL: Expected {'solutions' if should_have_solutions else 'no solutions'}")
                all_passed = False
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
            all_passed = False
    
    # Error handling
    print("\n[Test 6] Self-loop error handling")
    try:
        Graph2ColoringSolver([(0,0)], 1)
        print("  ✗ FAIL: Should reject self-loop")
        all_passed = False
    except ValueError:
        print("  ✓ PASS: Correctly rejected self-loop")
    
    print("\n" + "=" * 70)
    print("✓ ALL TESTS PASSED" if all_passed else "✗ SOME TESTS FAILED")
    print("=" * 70)
    
    return all_passed


def main():
    if len(sys.argv) > 1:
        mode = sys.argv[1]
        
        if mode == "--test":
            print("GRAPH 2-COLORING: Test Suite Only\n")
            test_graph_2_coloring()
            
        elif mode == "--demo":
            print("GRAPH 2-COLORING: Complexity Demo Only\n")
            demonstrate_exponential_growth()
            
        else:
            print(f"Unknown option: {mode}")
            print("\nUsage: python graph_2_coloring.py [--test|--demo|--all]")
            print("  --test : Run test suite only")
            print("  --demo : Run complexity demo only")
            print("  --all  : Run both (same as no argument)")
            
    else:
        # Default: run both
        print("GRAPH 2-COLORING: O(2^n) ALGORITHM\n")
        test_graph_2_coloring()
        demonstrate_exponential_growth()



if __name__ == "__main__":
    main()
