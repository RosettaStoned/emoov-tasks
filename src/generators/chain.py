
def chain(iterable_one, iterable_two):

    for elem in iterable_one:
        yield elem
    for elem in iterable_two:
        yield elem
