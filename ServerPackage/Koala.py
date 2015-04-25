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

list = [[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],
        [2,3],[2,4],[2,5],[2,6],[2,7],[2,8],
        [3,4],[3,5],[3,6],[3,7],[3,8],
        [4,5],[4,6],[4,7],[4,8],
        [5,6],[5,7],[5,8],
        [6,7],[6,8],
        [7,8]
        ]

list1 = [[1,2],[1,3],[1,4],
         [2,3],[2,4],
         [3,4]
        ]
print str(unique_match_sort(list1))
# print str(sort([], list1))