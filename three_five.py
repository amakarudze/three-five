"""Program that prints numbers from 1 to 100. For multiples of 3, the program prints 'Three' instead of the number and
 for the multiples of 5 prints 'Five' instead. For multiples of both 3 and 5, the program prints 'ThreeFive'.

 Author: Anna Makarudze
 Created: 25/02/2020"""


def three_five():
    """Generate the list of numbers from 1 to 100

    >>> num_list = range(1, 101)
    >>> len(num_list)
    100
    >>>

    Check if number is multiple of both 3 and 5
    >>> number1 = 15
    >>> if number1 % 3 == 0 and number1 % 5 ==0:
    ...    print("ThreeFive")
    ThreeFive
    >>>

    Check if number is multiple of 3
    >>> number2 = 6
    >>> if number2 % 3 == 0:
    ...    print("Three")
    Three
    >>>

    Check if number is multiple of 5
    >>> number3 = 10
    >>> if number3 % 5 == 0:
    ...    print("Five")
    Five
    >>>

    Print numbers which are neither multiples of 3 nor 5
    >>> number4 =98
    >>> print(number4)
    98
    >>>
    """

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("ThreeFive")
        elif i % 3 == 0:
            print("Three")
        elif i % 5 == 0:
            print("Five")
        else:
            print(i)


three_five()


if __name__ == "main":
    import doctest
    doctest.testmod()
