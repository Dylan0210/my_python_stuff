#  prints the number of times that the substring occurs in the given string
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count = count+1
    return(count)
