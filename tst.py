def create_lists(input_list):
    result = []
    for i in range(len(input_list)):
        sublist = input_list[i:] + input_list[:i]
        result.append(sublist)
    return result

input_list = "И.Р.Худ, С.А.Науман, Н.Н.Священко, Ч.Е.Нонова".split(', ')
result_lists = create_lists(input_list)
print(*[', '.join(x) for x in result_lists], sep='\n')