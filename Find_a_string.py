def count_substring(string, sub_string):
    count=0
    #print(len(string),len(sub_string))
    for i in range(0, len(string)-len(sub_string)+1):
        # test for presence of first char of sub_string at ith position of string
        if string[i] == sub_string[0]:
            flag=1
            for j in range (0, len(sub_string)):
                if string[i+j] != sub_string[j]:
                    flag=0
                    break
            if flag==1:
                count += 1
    return count
