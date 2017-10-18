import string

ABC = string.ascii_uppercase
abc = string.ascii_lowercase

def ceaser_cipher(text, offset):

    trns = str.maketrans(abc + ABC, abc[offset:] + abc[:offset] + ABC[offset:] + ABC[:offset])
    return text.translate(trns)

def encrypt(offset):
    """decorator function that provides Ceaser Cipher encryption"""	

    def decorator(func):

        def new_func(*args, **kwargs):

            text = func(*args, **kwargs)
            if not isinstance(text, str):
                raise TypeError('Decorated function must return str!')

            return ceaser_cipher(text, offset)

        new_func.__name__ = func.__name__
        return new_func

    return decorator

