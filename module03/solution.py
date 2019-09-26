def sum_of_digits(n):
    num_str = str( abs(n) )
    sum = 0
    for i in range( len(num_str) ):
        sum += int(num_str[i])
    return sum

def to_digits(n):
    list=[int(i) for i in str(n)]
    return list


def count_vowels(str):
    sum=0
    list=("a","e","i","o","u","y")
    for i in str:
        if i.lower() in list:
            sum += 1
    return sum