def multi_table(table, limit):
    output = []
    table =  int(table)
    limit = int(limit)
    for i in range(1, limit + 1):
        result = table * i
        output.append(result)
    print(output)
    return output

"""
table = 3
limit = 4 



"""


