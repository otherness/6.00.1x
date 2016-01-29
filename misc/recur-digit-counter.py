def ndigits(x):
    '''
    function returns number of digits in number x
    '''
    
    assert type(x) == int               # check if input parameter has type int
    
    if abs(x) < 10:                     # base case x < 10
        return 1
    return 1 + ndigits(int(x/10.0))     # divide number by 10 until number would be < 10
