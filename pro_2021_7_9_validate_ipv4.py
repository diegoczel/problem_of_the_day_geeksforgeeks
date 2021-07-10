""" Validate ip
Problema retirado do site geeksforgeeks em 2021/7/9.
Resolvido por Diego Czel Stepanha.

Write a program to Validate an IPv4 Address. According to Wikipedia, IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots, e.g., 172.16.254.1 . The generalized form of an IPv4 address is (0-255).(0-255).(0-255).(0-255). Here we are considering numbers only from 0 to 255 and any additional leading zeroes will be considered invalid.

Your task is  to complete the function isValid which returns 1 if the ip address is valid else returns 0. The function takes a string s as its only argument .

Example 1:

Input:
ip = 222.111.111.111
Output: 1
Example 2:

Input:
ip = 5555..555
Output: 0
Explanation: 5555..555 is not a valid
ip address, as the middle two portions
are missing.
Your Task:
Complete the function isValid() which takes the string s as an input parameter and returns 1 if this is a valid ip address otherwise returns 0.

Expected Time Complexity: O(N), N = length of string.
Expected Auxiliary Space: O(1)

Constraints:
1<=length of string <=50
"""
def isValid(s):
    #code here
    s = s.split('.')
    # tamanho do ip deve ser de 4 todos inteiros
    if len(s) != 4 or all(map(str.isdecimal, s)) == False:
        return 0
    else:
        for ind in s:
            n = int(ind)
            """
            len(ind) > 3
                cuida de str's like '0000'
            (n < 0 or n > 255)
                cuida do range do ip
            (len(ind) == 2 and ind[0] == '0')
                cuida de ip's like '04'
            (len(ind) == 3 and ind[0] == '0')
                cuida de ip's like '010', '001'
                * não precisa verificar ind[1] pois já
                é tratado no len(ind) == 2
            """
            if len(ind) > 3 or \
                (n < 0 or n > 255) or \
                (len(ind) == 2 and ind[0] == '0') or \
                (len(ind) == 3 and ind[0] == '0'):
                return 0
        return 1
