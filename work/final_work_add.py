def add_func(num1,num2):

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

    i = max(length1,length2)

    carry = 0

    while(i > 0):
        if(int(number1[i-1]) + int(number2[i-1]) + carry > 9):
            result = str(int(number1[i-1]) + int(number2[i-1]) + carry)
            res_list.insert(0,(result[-1]))
            carry = 1

            if(i==1):
                result = str(int(number1[i-1]) + int(number2[i-1]) + carry)
                res_list[0]= result


        elif(int(number1[i-1]) + int(number2[i-1]) > 9):
            result = str(int(number1[i-1]) + int(number2[i-1]))
            res_list.insert(0,(result[-1]))
            carry = 1

        else:
            result = str(int(number1[i-1]) + int(number2[i-1]) + carry)
            res_list.insert(0,(result[-1]))
            carry = 0

        i -=1

    final_output = ('').join(res_list)
    return (int(final_output))

print(add_func('99990' , '9898986875'))
