def sub_func(num1,num2):

    res_list = []

    number1 = str(num1)
    number2 = str(num2)
    length1 = len(str(number1))
    length2 = len(str(number2))

    if(length1 > length2):
        while(length1 > length2):
            number2 = '0' + number2
            length2 += 1

    if(length2 > length1):
        while(length2 > length1):
            number1 = '0' + number1
            length1 += 1

    numb_list1 = [int(x) for x in number1]
    numb_list2 = [int(x) for x in number2]

    i = max(length1,length2)

    borrow = 0

    while(i > 0):
        if(num1 > num2):
            if(numb_list1[i-1] - numb_list2[i-1] - borrow < 0):
                result = str(numb_list1[i-1]+10 - numb_list2[i-1])
                res_list.insert(0,str(result))
                numb_list1[i-2] -=1

            else:
                result = str(numb_list1[i-1] - numb_list2[i-1] - borrow)
                res_list.insert(0,str(result))
                borrow = 0

        else:
            if(numb_list2[i-1] - numb_list1[i-1] - borrow < 0):
                result = str(numb_list2[i-1]+10 - numb_list1[i-1])
                res_list.insert(0,str(result))
                numb_list2[i-2] -=1

            else:
                result = str(numb_list2[i-1] - numb_list1[i-1] - borrow)
                res_list.insert(0,str(result))
                borrow = 0

        i -=1


    if(num1<num2):
        return(int(('').join(res_list).lstrip('0'))* -1)

    else:
        return(int(('').join(res_list).lstrip('0')))

print(sub_func(653653,543587576))
