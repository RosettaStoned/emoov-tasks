import os
import sys
import pathlib
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_DIR = '{}/../logs/'.format(BASE_DIR)

def log(filename, **kwargs):

    def decorator(func):

        pathlib.Path(LOGS_DIR).mkdir(parents=True, exist_ok=True)
        file_path = '{}/{}'.format(LOGS_DIR, filename)

        func_name = kwargs.get('name') or func.__name__

        now = datetime.now()

        try:

            with open(file_path, 'a+') as fd:

                if kwargs.get('msg') is None:
                    fd.write('{} was called at: {}\n'.format(func_name, now))
                else:
                    fd.write('{} was called and took {} seconds to complete\n'.format(func_name, now, kwargs.get('msg')))

            fd.close()

        except EnvironmentError as e:

            sys.stderr.write('Error: {0}\n'.format(str(e, 'utf-8')))
            pass

        return func

    return decorator





