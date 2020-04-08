"""
Read an integer .
Without using any string methods, try to print the following:
123..N
Note that "" represents the values in between.
Input Format
The first line contains an integer .
Output Format
Output the answer as explained in the task.
Sample Input 0
3
Sample Output 0
123
------
xrange()
Renames xrange() to range() and wraps existing range() calls with list.
"""

"""
X = 'spam'
for item in X:print(item,end= '')
"""
if __name__ == '__main__':
    n = int(input())

X = range(1,n+1)
for item in X:print(item, end ='')
