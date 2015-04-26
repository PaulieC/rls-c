__author__ = 'paulie'


def unique_match_sort(match_list):
    temp_list = match_list
    return_list = []
    while temp_list:
        return_list.append(temp_list.pop(0))
        return_list.append(temp_list.pop(len(temp_list) - 1))
    return return_list

def sort(sorted_list, match_list):
    """
    :param sorted_list: list
    :param match_list: list
    :return:
    """
    if len(match_list) == 1:
        sorted_list.append(match_list[0])
        return sorted_list
    else:
        limit = len(match_list)/2
        found = 0
        for match in match_list:
            if sorted_list:
                name1 = sorted_list[len(sorted_list) - 1][0]
                name2 = sorted_list[len(sorted_list) - 1][1]
                if match[0] == name1 or match[0] == name2:
                    pass
                elif match[1] == name1 or match[1] == name2:
                    pass
                else:
                    sorted_list.append(match)
                    match_list.remove(match)
                    found += 1
            else:
                sorted_list.append(match)
                match_list.remove(match)
                found += 1
            if found == limit:
                break
        return sort(sorted_list, match_list)

list8 = [[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],
         [2,3],[2,4],[2,5],[2,6],[2,7],[2,8],
         [3,4],[3,5],[3,6],[3,7],[3,8],
         [4,5],[4,6],[4,7],[4,8],
         [5,6],[5,7],[5,8],
         [6,7],[6,8],
         [7,8]
        ]

list6 = [[1,2],[1,3],[1,4],[1,5],[1,6],
         [2,3],[2,4],[2,5],[2,6],
         [3,4],[3,5],[3,6],
         [4,5],[4,6],
         [5,6],
        ]

list4 = [[1,2],[1,3],[1,4],
         [2,3],[2,4],
         [3,4]
        ]

"""
    1. create a 2-dimensional array filled with 0's in range(num_players - 1)
    2. find a unique match in row 1.
    2a. find another unique match avoiding the row numbers of the previous player numbers
    2b. find another unique match avoiding the row numbers of all of the previous numbers
    3. continue step 2x until we have found (num_players/2) unique matches
    4. replace these matches with 0's in the 2-d array
    5. begin the search again
    [[1,2],[1,3],[1,4],
     [2,3],[2,4],  0
     [3,4],  0  ,  0
    ]
    --> [1,2], [3,4]
    [[1,3],[1,4],
     [2,3],[2,4],  0
       0  ,  0
    ]
    --> [1,3],
"""

# print str(unique_match_sort(list4))
# print str(sort([], list1))