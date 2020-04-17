"""
map built-in function applies a function to items in a sequence and collects all
the results in a new list.
list(map(abs,[-1,2,0,1,2]))
"""
if __name__ == '__main__':
    n = int(input())
    input_line = input()
    integer_list = map(int, input_line.split())
    t = tuple(integer_list)
    print(hash(t))
