from jovian.pythondsa import evaluate_test_cases

#                                                                                                  LINEAR SEARCH / BRUTE SEARCH

#                                                                                        METHOD OR STRATEGY TO APPLY IN CODING

# 1. STATE THE PROBLEM CLEARLY, IDENTIFY THE INPUT AND OUTPUT FORMATS.
# 2. COME UP WITH SOME EXAMPLES INPUTS AND OUTPUTS, COVER ALL EDGE CASES.
# 3. COME UP WITH CORRECT SOLUTIONS IN PLAIN ENGLISH.
# 4.IMPLEMENT SOLUTION AND TEST IT USING EXAMPLE INPUTS, FIX BUGS IF ANY.
# 5.ANALYZE THE ALGORITHM COMPLEXITY AND IDNTIFY INEFFICIENCIES. IF ANY.
# 6. APPLY THE RIGHT TECHNIQUE TO OVERCOME THE INEFFICIENCY. REPEAT STEPS 3 TO 6

#                                                                                                                       PROBLEM 1

# 'ALICE HAS SOME CARDS WITH NUMBERS WRITTEN ON THEM. SHE ARRANGES THE CARD IN DECREASING ORDER, AND LAYS THEM OUT FACE DOWN IN A SEQUENCE ON A TABLE. SHE CHALLENGES BOB TO PICK OUT THE CARD CONTAINING A GIVEN NUMBER BY TURNING OVER AS FEW CARDS AS POSSIBLE. WRITE A FUNCTION TO HELP BOB LOCATE THE CARD.'

#                                                                                                                       SOLUTION

# STEP 1 - SUMMARY:  WE NEED TO WRITE A PROGRAM TO FIND THE POSITION OF A GIVEN NUMBER IN A LIST OF NUMBERS IN DECREASING ORDER. WE ALSO NEED TO MINIMIZE THE NUMBER OF TIMES WE ACCESS ELEMENTS FROM THE LIST.

# STEP 2 -INPUTS AND OUTPUTS:
#     1. CARDS: decreasing number e.g [13,11,10,7,4,3,1]
#     2. QUERY: RETURNED VALUE TO BE DETERMINED. eg 7

#     OUTPUTS
#         3. POSITIONS: position of given number in the list eg 3

# def locate_card(cards, query):
#     pass

# note: i used pass cuz its serve same definition as declaring return in js

# STEP 2 PART B: EDGE CASES

# cards = [13, 11, 10, 7, 4, 3, 1, 0]
# query = 7,
# output = 3

# compare yourfunction with expected output

# result = locate_card(cards, query)
# print(result)

# result == output

test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

output = test['output']

#  locate_card(**test['input']) == test['output']

#                                                                                VARIATIONS TO ENCOUNTER

# 1. THE NUMBER QUERY OCCURS SOMEWHERE IN THE MIDDLE OF THE list
# 2. QUERY IS THE FIRST NUMBER
# 3. QUERY IS THE LAST NUMBER
# 4. CONTAINS ONLY ONE ELEMENT WHICH IS THE query
# 5. DOES NOT CONTAIN query
# 6. LIST CARD IS EMPTY
# 7. CONTAINS REPEATING NUMBERS
# 8. REPEATING QUERY NUMBERS

#                                                                             VARIATIONS TO ENCOUNTER WITH CODE

tests = []

# 1. THE NUMBER QUERY OCCURS SOMEWHERE IN THE MIDDLE OF THE list

tests.append(test)

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

# 2. QUERY IS THE FIRST NUMBER

tests.append({'input': {'cards': [4, 3, 1, 0], 'query': 4}, 'output': 0})

# 3. QUERY IS THE LAST NUMBER

tests.append({
    'input': {
        'cards': [4, 3, -9, -127],
        'query': -127
    },
    'output': 3
})

# 4. CONTAINS ONLY ONE ELEMENT WHICH IS THE query

tests.append({'input': {'cards': [4], 'query': 4}, 'output': 0})

# 5. DOES NOT CONTAIN query

tests.append({'input': {'cards': [4, 3, -9, -127], 'query': 5}, 'output': -1})

# 6. LIST CARD IS EMPTY

tests.append({'input': {'cards': [], 'query': 5}, 'output': -1})

# 7. CONTAINS REPEATING NUMBERS

tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 6
})

# 8. REPEATING QUERY NUMBERS

tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

# 3.                             COME UP WITH CORRECT SOLUTIONS IN PLAIN ENGLISH.

# 1. CREATE A VARIABLE POSITION 0
# 2a. check if cards length greaterthan zero
# 2. CHECK IF NUMBER INDEX POSITION EQUALS query
# 3. IF IT DOES.. RETURN POSITION NUMBER ELSE
# 4. INCREMENT THE VALUE OF POSITION BY 1 AND REPEAT STEPS 2 TO 5 TILL WE REACH THE LAST POSITION
# 5. IF THE NUMBER NOT FOUND, RETURN -1.

# 4.            IMPLEMENT SOLUTION AND TEST IT USING EXAMPLE INPUTS, FIX BUGS IF ANY.


def locate_card(cards, query):
    # 1. CREATE A VARIABLE POSITION 0
    position = 0
    # 2a. check if cards length greater than zero
    while position < len(cards):
        # 2. CHECK IF NUMBER INDEX POSITION EQUALS query
        if cards[position] == query:
            # 3. IF IT DOES.. RETURN POSITION NUMBER ELSE
            return position
        # 4. INCREMENT THE VALUE OF POSITION BY 1 AND REPEAT STEPS 2 TO 5 TILL WE REACH THE LAST POSITION
        position = position + 1
        # 5. IF THE NUMBER NOT FOUND and we reached the end of card, RETURN -1.
    return -1


# evaluate_test_cases(locate_card, tests)

# 5.                                    ANALYZE THE ALGORITHM COMPLEXITY AND IDNTIFY INEFFICIENCIES. IF ANY.

# 6.                                     APPLY THE RIGHT TECHNIQUE TO OVERCOME THE INEFFICIENCY. REPEAT STEPS 3 TO 6

# To find the inefficiency we use binary search.
# 1. FIND THE MIDDLE ELEMENT OF THE LIST.
# 2. IF IT MATCHES QUERIED NUMBER, RETURN THE MIDDLE POSITION AS THE ANSWER.
# 3. IF IT IS LESS THAN THE QUERIED NUMBER, THEN SEARCH THE FIRST HALF OF THE LIST.
# 4. IF IT IS GREATER THAN THE QUERIED NUMBER, THEN SEARCH THE SECOND HALF OF THE LIST.
# 5. IF NO MORE ELEMENTS REMAIN, RETURN -1

#                                                                                                   SOLUTION


def locate_binary_card(cards, query):
    lo = 0
    hi = len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]

        print('lo :', lo, 'hi :', hi, 'mid :', mid, 'mid_number :', mid_number,
              'query :', query)

        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1
    return -1


evaluate_test_cases(locate_binary_card, tests)
