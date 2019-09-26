def sum_of_digits(n):
    num_str = str(abs(n))
    sum = 0
    for i in range(0, len(num_str)):
        sum += int(num_str[i])
    return sum

def to_digits(n):
    list=[int(i) for i in str(n)]
    return list


def count_vowels(str):
    list=("a","e","i","o","u","A","E","I","O","U")
    for i in str:
        if i in list:
            return