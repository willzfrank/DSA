from jovian.pythondsa import evaluate_test_cases

# QUESTION

question = 'Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.'

test = {'input': {'nums': [1, 3, 5, 6], 'target': 5}, 'output': 2}

tests = []
output = test['output']

# 1. THE NUMBER QUERY OCCURS SOMEWHERE IN THE MIDDLE OF THE list

tests.append(test)

tests.append({'input': {'nums': [1, 3, 5, 6], 'target': 5}, 'output': 2})

# 2. QUERY IS THE FIRST NUMBER

tests.append({'input': {'nums': [1, 3, 5, 6], 'target': 2}, 'output': 1})

# 3. QUERY IS THE LAST NUMBER

tests.append({'input': {'nums': [1, 3, 5, 6], 'target': 7}, 'output': 4})


def locate_binary_num(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_number = nums[mid]

        # print('left :', left, 'right :', right, 'mid :', mid, 'mid_number :',
        #       mid_number, 'target :', target)
        if mid_number == target:
            return mid
        elif mid_number < target:
            left = mid + 1
        elif mid_number > target:
            right = mid - 1
    return left


evaluate_test_cases(locate_binary_num, tests)
