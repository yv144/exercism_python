# Implement a binary search algorithm.

def find(search_list: list, value: int) -> int:
    start = 0
    end = len(search_list)
    i = 0
    index_db = [-1,]

    if len(search_list) == 0:
        raise ValueError ("value not in array") 

    while True:
        index = (start + end) // 2

        index_db.append(index)
        if index_db[-1] == index_db[-2]:
            raise ValueError ("value not in array") 

        obtained = search_list[index]
        if value == obtained:
            return index
        elif value < obtained:
            end = index
        elif value > obtained:
            start = index
    raise ValueError ("value not in array")
