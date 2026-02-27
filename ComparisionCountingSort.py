def comparison_counting_sort(A):
    """
    Sorts an array by comparison counting.
    Input: An array A of orderable elements.
    Output: Array S of A's elements sorted in nondecreasing order.
    """
    n = len(A)
    
    # Initialize the Count array with zeros
    Count = [0] * n
    
    # Initialize the output array S with placeholders
    S = [0] * n
    
    # Compare every pair (i, j) exactly once
    for i in range(n - 1):
        for j in range(i + 1, n):
            # This is the missing part of your pseudocode!
            if A[i] < A[j]:
                Count[j] += 1  # A[j] is strictly greater
            else:
                Count[i] += 1  # A[i] is greater than or equal to A[j]
                
    # Place elements into their correct sorted positions
    for i in range(n):
        S[Count[i]] = A[i]
        
    return S

# --- Let's test it with the textbook example ---
if __name__ == "__main__":
    A = [62, 31, 84, 96, 19, 47]
    sorted_A = comparison_counting_sort(A)
    
    print(f"Original Array: {A}")
    print(f"Sorted Array:   {sorted_A}")
