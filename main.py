
def isSubset(num1, num2):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def main():
    num1 = [20, 30, 35]
    num2 = [5, 20, 30, 35, 50]
    ret = isSubset(num1, num2)
    print(f'Your return value is {ret}')  # True

    num1 = [1, 3, 2]
    num2 = [1, 2, 3, 4, 5]
    ret = isSubset(num1, num2)
    print(f'Your return value is {ret}')  # False

    num1 = [1, 4, 5]
    num2 = [1, 2, 3, 4, 5]
    ret = isSubset(num1, num2)
    print(f'Your return value is {ret}')  # False

    num1 = [1, 3, 2]
    num2 = [4, 1, 3, 2, 5]
    ret = isSubset(num1, num2)
    print(f'Your return value is {ret}')  # True


if __name__ == '__main__':
    main()
