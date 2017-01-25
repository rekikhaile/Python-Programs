def test(fn):
    print(fn(1, 5, 6) == (-3, -2))
    print(fn(1, -5, 6) == (2, 3))
    print(fn(0, 5, 10) == (-2, None))
    print(fn(1, -2, -15) == (-3, 5))
    print(fn(1, 0, 16) == (None, None))


#test(fn)
    
