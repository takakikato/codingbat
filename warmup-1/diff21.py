def diff21(n):
    """
    Given an int n, return the absolute difference between n and 21, except return double the 
    absolute difference if n is over 21
    """
    if isinstance(n, int) == False:
        print('You must enter an integer')
    else:
        if n <= 21:
            return 21 - n
        else:
            return (n - 21) * 2


def main():
    n = int(input('Enter an integer: '))
    print(diff21(n))

    print(diff21(19))
    print(diff21(10))
    print(diff21(21))


if __name__ == "__main__":
    main()