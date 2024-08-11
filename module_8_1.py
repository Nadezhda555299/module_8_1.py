def add_everything_up(a, b):
    try:
        print(a + b)
        # ((a.isinteger() or a.isfloat()) and b.isstring()) or ((b.isinteger() or b.isfloat()) and a.isstring()):
    except TypeError:
        print(str(a) + str(b))

add_everything_up(101, 'first')
add_everything_up('second, ', 101.101)
add_everything_up(2024.2025, 1900)
