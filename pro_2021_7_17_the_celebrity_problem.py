"""the celebrity problem
Problema retirado do site geeksforgeeks em 2021/07/17
Resolvido por Diego Czel Stepanha

A celebrity is a person who is known to all but does not know anyone at a party. If you go to a party of N people, find if there is a celebrity in the party or not.
A square NxN matrix M[][] is used to represent people at the party such that if an element of row i and column j  is set to 1 it means ith person knows jth person. Here M[i][i] will always be 0.
Note: Follow 0 based indexing.
 

Example 1:

Input:
N = 3
M[][] = {{0 1 0},
         {0 0 0}, 
         {0 1 0}}
Output: 1
Explanation: 0th and 2nd person both
know 1. Therefore, 1 is the celebrity. 

Example 2:

Input:
N = 2
M[][] = {{0 1},
         {1 0}}
Output: -1
Explanation: The two people at the party both
know each other. None of them is a celebrity.

Your Task:
You don't need to read input or print anything. Complete the function celebrity() which takes the matrix M and its size N as input parameters and returns the index of the celebrity. If no such celebrity is present, return -1.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
2 <= N <= 3000
0 <= M[][] <= 1

"""
def celebrity(M, n):
    # index of celebrity
    c = -1
    # find first celebrity candidate that does not know anyone [0, 0, ...]
    for ind in range(n):
        # OPTION if 1 not in M[ind]
        if all(map(lambda x: x == 0, M[ind])):
            c = ind
            break
    if c == -1:
        return -1
    else:
        # validate if all person's know celebrity
        for ind in range(n):
            # M[ind][c] == 0 person do not know celebrity, then, no such celebrity present
            if M[ind][c] == 0 and ind != c:
                return -1
        return c
                
            

print(celebrity([[0, 1, 0], [0, 0, 0], [0, 1, 0]], 3))
print(celebrity([[0, 1], [1, 0]], 2))