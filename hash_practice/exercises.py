
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """
    string_dict = {}
    for string in strings:
        key = ''.join(sorted(string))

        if key in string_dict.keys():
            string_dict[key].append(string)
        else:
            string_dict[key] = [string]
        
    return list(string_dict.values())

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n) + O(n log n)??
        Space Complexity: O(n)
    """
    frequency_map = {}
    return_list = []

    for num in nums:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1

    max_values = sorted(frequency_map.values(), reverse=True)
        
    for key, value in frequency_map.items():
        if value in max_values[:k] and (len(return_list) < k):
            return_list.append(key)

    return return_list




def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """
    # check if the input has too many rows
    if len(table) > 9:
        return False
    for i in range(len(table)):
        row_dictionary = {}
        column_dictionary = {}
        subgrid_dictionary = {}

        # check if the input has too many columns
        if len(table[i]) > 9:
            return False
        
        for j in range(len(table[i])):
            # check row
            if table[i][j] != "." and table[i][j] in row_dictionary:
                return False
            row_dictionary[table[i][j]] = "yay!"

            # check column
            if table[j][i] != "." and table[j][i] in column_dictionary:
                return False
            column_dictionary[table[j][i]] = "yay!"

            # check sub-grid
            # ????
    return True

            




