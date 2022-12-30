if __name__ == '__main__':
    a = int(input())
    b = int(input())
    assert type(a) and type(b) == int
    print("{0}\n{1}\n{2}".format(a+b,a-b,a*b))
