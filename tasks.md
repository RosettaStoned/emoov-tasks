# Decorator Problems

## @accepts
Make a decorator ``accepts`` that takes as many arguments as the function takes. That decorator specify the types of the arguments that your function takes. If any of the arguments does not match the type in the decorator raise a ``TypeError``

### Examples
```python
@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

say_hello(4)

TypeError: Argument 1 of say_hello is not str!
```

```python
@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

say_hello("Spicy Paprika")
```

```python
@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True

deposit("Rostislav", 10)
```

Note that this is just a nice example. In real life you don't want use this!

Think of more vanilla way of building input data validation using python > 3.5.

## @encrypt(key)

Make a decorator ``encrypt`` that takes an integer. The decorator should encrypts the returned string of a function using the [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher). That integer is the encryptions key.

### Example

```python
@encrypt(2)
def get_low():
    return "Get get get low"

get_low()

Igv igv igv nqy
```

## @log(file_name)
Make a decorator ``log`` that takes an ``file_name`` and writes in to this file a log. New line for every call of the decorated function. 


### Example

```python
@log('log.txt')
@encrypt(2)
def get_low():
    return "Get get get low"

get_low()

Igv igv igv nqy
```

And the log file should look like this:

```
get_low was called at 2015-08-04 02:51:41.929980
get_low was called at 2015-08-04 02:51:45.992980
get_low was called at 2015-08-04 02:51:42.999923
```

## @performance(file_name)
Make a decorator ``performance`` that takes an ``file_name`` and writes in to this file a log. New line for every call of the decorated function. This decorator should log the time needed for the decorated function to execute.

### Example

```python
@performance('log.txt')
def something_heavy():
    sleep(2)
    return "I am done!"

something_heavy()

I am done!
```

And the log file should look like this:

```
something_heavy was called and took 2.00 seconds to complete
something_heavy was called and took 2.10 seconds to complete
```

# Generators

## chain

Implement a function that takes two iterables and returns another one that concatenate the two iterables. 


```python
def chain(iterable_one, iterable_two):
    pass
```

### Example

```python
>>> list(chain(range(0, 4), range(4, 8)))
[0, 1, 2, 3, 4, 5, 6, 7]
```

## compress

Implement a function that takes one iterables and one iterable mask. The mask is an collection that contains only ``True`` or ``False``

This function returns only this objects from the first collection that have ``True`` on their position in the mask.


```python
def compress(iterable, mask):
    pass
```

### Example

```python
>>> list(compress(["Dimitar", "Rostislav", "emoov"], [False, False, True]))
["emoov"]
```

## cycle

Implement a function that takes an iterable and returns endless concatenation of it.


```python
def cycle(iterable):
    pass
```

```python
>>> endless = cycle(range(0,10))
for item in endless:
    print(item)
```

## Book Reader
You have some text files. They represent a book. Our book contains chapters. Each chapter starts with ``#`` at the beginning of the line. (Markdown book)

Our book is made of many files. Each file has its number ``001.txt, 002.txt, 003.txt``

Each file may contain one or more chapters.

[Link to the book](https://gist.github.com/rbagrov/bb38d78ddcacdca1e79a48ec22797739#file-book-zip)

Write a program that displays on the console each chapter. You can only move forwards using the ``space button``.

Try not to load the whole book in the memory. Use generator!

## Book Generator
Make a python program that generates books.

Your program should take the following parameters.

- Chapters count
- Chapter length range (in words)

The words should be with random length and random char. The format of the book should be: chapters with paragraphs with sentenses with punctuation. Try to place some new lines in the chapters at random positions. Title and numerate the chapters. The whole book must be in one file.


Try to generate bigger book. Like 1-2G, and try to pass it to the previous program.