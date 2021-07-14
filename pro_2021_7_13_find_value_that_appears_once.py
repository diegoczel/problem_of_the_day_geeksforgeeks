"""Problem: Find the element that appears once.
Problema retirado do site geeksforgeeks em 2021/7/14
Resolvido por Diego Czel Stepanha

Given a sorted array A[] of N positive integers having all the numbers
occurring exactly twice, except for one number which will occur only once.
Find the number occurring only once.

Example 1:

Input:
N = 5
A = {1, 1, 2, 5, 5}
Output: 2
Explanation: 
Since 2 occurs once, while
other numbers occur twice, 
2 is the answer.
Example 2:

Input:
N = 7
A = {2, 2, 5, 5, 20, 30, 30}
Output: 20
Explanation:
Since 20 occurs once, while
other numbers occur twice, 
20 is the answer.
Your Task:
You don't need to read input or print anything.
Your task is to complete the function search() which takes
two arguments(array A and integer N) and
returns the number occurring only once.

Expected Time Complexity: O(Log(N)).
Expected Auxiliary Space: O(1).

Constraints
0 <   N  <= 10^6
0 <= A[i] <= 10^9
"""
def search(A, N):
    # len(A) is 1
    if N == 1:
        return A[0]
    # value unique is in the end
    if A[N-1] != A[N-2]:
        return A[N-1]
    for x in range(0, N, 2):
        """A = [1, 1, 2, 5, 5]
        when (A[2] == 2) is != of (A[3] == 5) then:
        return A[2] == 2
"""
        if A[x] != A[x + 1]:
            return A[x]

print(search([1, 1, 2, 5, 5], 5))
print(search([1, 1, 5, 5, 2], 5))
print(search([2, 2, 5, 5, 20, 30, 30], 7))
print(search([20, 2, 2, 5, 5, 30, 30], 7))