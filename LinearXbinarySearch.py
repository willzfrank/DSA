from jovian.pythondsa import evaluate_test_case

test = {'input': {'num': [11, 14, 19, 25, 29, 3, 5, 6, 7, 9]}, 'output': 5}

output = test['output']

num = test['input']['num']
output = test['output']


def count_rotations_linear(num):
    # created the position as zero
    position = 0
    # checked if the total number of num cards is greater than zero to start
    while position < len(num):
        if num[position] > num[position + 1]:
            # if so then i checked if the cards at left position is greater than cards at right position
            print('position :', position)
            print('num :', num)
            # else i believed i have found the position
            return position + 1
        print('position for left:', num[position])
        print('position for right:', num[position + 1])
        print('')
        # if its true i increased the position index
        position += 1

    # or prolly i havent
    return 0


evaluate_test_case(count_rotations_linear, test)

# BINARY SEARCH

# To find the inefficiency we use binary search.
# 1. FIND THE MIDDLE ELEMENT OF THE LIST.
# 2.CHECK IF THE NUMBER AT THE LEFT IS GREATER THAN THE LAST NUMBER AT THE RIGHT
# 3.  IF IT IS GREATER THAN THE QUERIED NUMBER, THEN SEARCH THE SECOND HALF OF THE LIST
# 4. IF IT IS LESS THAN THE QUERIED NUMBER, THEN SEARCH THE FIRST HALF OF THE LIST.
# 5. IF NO MORE ELEMENTS REMAIN, RETURN -1


def locate_binary_num(num):
    lo = 0
    hi = len(num) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = num[mid]

        print('lo :', lo, 'hi :', hi, 'mid :', mid, 'mid_number :', mid_number,
              'num :', num)

        if mid_number > num[hi] :
            lo = mid + 1
        elif mid_number < num[hi]:
            hi = mid - 1
    return 0


evaluate_test_case(locate_binary_num, test)