# Parse and evaluate simple math word problems returning the answer as an integer.

OPERATORS = ["plus","minus","multiplied_by","divided_by"] 

def check_number_operator(keyword:str) -> list[bool,bool]:
    try:
        is_number = int(keyword)**0
        is_opeator = False
    except:
        is_number = False
        if keyword in OPERATORS:
            is_opeator = True  
        else:
            is_opeator = False
    if not any([is_number,is_opeator]):
        raise ValueError("unknown operation")
    return [is_number,is_opeator]


def answer(question:str)->int:
    question = question.replace("multiplied by","multiplied_by").replace("divided by","divided_by")
    data = question[8:-1:].split()


    try:
        total = int(data[0])
    except:
        if len(data) == 0:
            raise ValueError("syntax error")
        elif len(data)>0 and data[0] not in OPERATORS:
            raise ValueError("unknown operation")

    if len(data)>1:
        for index,item in enumerate(data):
            test_resuls = check_number_operator(item)
            if index % 2 == 1 and test_resuls[0]:
                raise ValueError("syntax error")
            if index % 2 == 0 and test_resuls[1]:
                raise ValueError("syntax error")
        
        if len(data)%2==0:
            raise ValueError("syntax error")

        for rel_index, value in enumerate(data[2::2]):

            try:
                num = int(value)
            except:
                raise ValueError("syntax error")

            abs_index_of_operator = rel_index*2+1
            operator = data[abs_index_of_operator]

            if operator == "plus":
                total += num
            elif operator == "minus":
                total -= num
            elif operator == "multiplied_by":
                total *= num
            elif operator == "divided_by":
                total /= num
            else:
                raise ValueError("unknown operation")
    if len(data)==2:
        raise ValueError("unknown operation")
    return total
