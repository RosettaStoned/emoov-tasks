
def accepts(*types):
        """decorator function that check and test arguments vs types"""

        def decorator(func):
            """inner decorator function"""

            """assert that count of types in decorator is equel to  count of args in decorated func"""
            assert len(types) == func.__code__.co_argcount

            def new_func(*args, **kwargs):

                """test args vs types"""
                arg_idx = 0
                for _arg, _type in zip(args, types):
                    arg_idx += 1
                    if not isinstance(_arg, _type):
                        raise TypeError('Argument {} of {} is not {}!'.format(arg_idx, func.__name__, _type.__name__)) 


                return func(*args, **kwargs)

            new_func.__name__ = func.__name__
            return new_func


        return decorator


