def find_num(number_list: list, number: int)->bool:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
        else:
            #Changing None to False has allowed False to be returned
            return False

result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)