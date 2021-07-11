""" Implement Atoi
Problema retirado do site geeksforgeeks em 2021/7/10.
Resolvido por Diego Czel Stepanha.

Your task  is to implement the function atoi. The function takes a string(str) as argument and converts it to an integer and returns it.

Note: You are not allowed to use inbuilt function.

Example 1:

Input:
str = 123
Output: 123

Example 2:

Input:
str = 21a
Output: -1
Explanation: Output is -1 as all
characters are not digit only.

Your Task:
Complete the function atoi() which takes a string as input parameter and returns integer value of it. if the input string is not a numerical string then returns 1..

Expected Time Complexity: O(|S|), |S| = length of string str.
Expected Auxiliary Space: O(1)

Constraints:
1<=length of S<=10
"""
def atoi(string):
    # Code here
    tam = len(string)
    if tam > 0:
        # cuida do '-' no inicio mudando o inicio do ind
        # ind 0 p/ string que não inicia com '-'
        # ind 1 p/ string que iniciam com '-' e tem len > 1, like -0, -1, -a
        #      p/ ignorar o '-' e seguir adiante
        ind = 1 if string[0] == '-' and tam > 1 else 0
        while ind < tam:
            x = string[ind]
            # se x for algo diferente de um numeral return -1
            if (x == '0' or x == '1' or x == '2' or x == '3' or \
                x == '4' or x == '5' or x == '6' or x == '7' or \
                x == '8' or x == '9' or x == '10') == False:
                return -1
            ind += 1
        """
        string[0] == '0' and tam > 1
            cuida das strings que iniciam com '0' e tem len > 1 like: '01', '0x'
        (tam > 2 and string[0] == '-' and string[1] == '0')
            cuida das strings[0] == '-' e strings[1] == '0' com len > 2 like: '-0x', '-01'
"""
        if (string[0] == '0' and tam > 1) or (tam > 2 and string[0] == '-' and string[1] == '0'):
            return -1
        else:
            return int(string)
    else:
        return -1
print(atoi('001'))
print(atoi('-001'))
print(atoi('0'))
print(atoi('-0'))
print(atoi('10'))
print(atoi('-10'))
