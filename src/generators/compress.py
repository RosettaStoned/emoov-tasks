
def compress(iterable, mask):

    return (i for i, m in zip(iterable, mask) if m)


