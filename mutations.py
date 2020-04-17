def mutate_string(string, position, character):
    # explode elements of S into a list
    l = list(s)
    l[int(i)] = c  # in place change
    # join elements of list together into a string with a blank delimeter
    s_new = ''.join(l)
    # return the variable that will be used by function
    return s_new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    # call the function
    s_new = mutate_string(s, int(i), c)
    print(s_new)
