def div42by(divdeBy):
    #we can handel using Try and Except

    try:
        return 42/divdeBy
    except ZeroDivisionError:
        print('Even greatest mathematicians failed to divide anything by nothing(0) Who u are ')
        return 'Assume the Answer is INFINITY'  #if not mentioned return statement here None will be printed


print(div42by(2))
print(div42by(0)) #error occures named as 'ZeroDivisionError:'
print(div42by(5))
