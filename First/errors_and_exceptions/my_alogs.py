def swap(l, i):
    len_l = len(l)
    t = l[i]
    l[i] = l[len_l - i - 1]
    l[len_l - i - 1] = t

def minimum(l):
    try:
        if len(l) == 0:
            raise ValueError("Empty list can't provide a minimum number")
        mini = l[0]
        for i in l:
            if mini > i:
                mini = i
        return mini
    except Exception as e:
        print("!!---An error occurred", e, '---!!')

#   Q1
def reverse_list(l):
    for i in range(len(l) // 2):
        swap(l, i)

# Q2
def count_even_odd(l):
    count_of_even = 0
    count_of_odd = 0
    for i in l:
        if i ^ 0 == 1:
            count_of_odd += 1
        else:
            count_of_even += 1

# Q3
def maximum(l):
    try:
        if len(l) == 0:
            raise ValueError("Empty list can't provide a maximum number")
        maxi = l[0]
        for i in l:
            if maxi < i:
                maxi = i
            return maxi
    except Exception as e:
        print("!!---An error occurred", e, '---!!')

# Q4
def second_maximum(l):
    try:
        if len(l) <= 1:
            raise ValueError("List size less than or equal to one can't provide a second maximum number")
        maxi = l[0]
        for i in l:
            if maxi < i:
                maxi = i
        second_maxi = minimum(l)
        for i in l:
            if i != maxi and i > second_maxi:
                second_maxi = i
        if maxi==second_maxi:
            raise ValueError("There is only one value repeating in the list, can't provide second maximum")
        return second_maxi
    except Exception as e:
        print("!!---An error occurred", e, '---!!')

# Q5
def mean(l):
    length_of_list = len(l)
    try:
        if length_of_list == 0:
            raise ValueError("Empty list can't provide a mean value")
        sum_of_numbers_in_list = 0
        for i in l:
            sum_of_numbers_in_list += i
        mean = sum_of_numbers_in_list/length_of_list
        return mean
    except Exception as e:
        print("!!---An error occurred", e, '---!!')

# Q6
def find_in_range(l,start, end):
    try:
        my_list = []
        for i in l:
            if i >= start and i <= end:
                my_list.append(i)
        return my_list
    except Exception as e:
        print('Error occurred - ', e)
