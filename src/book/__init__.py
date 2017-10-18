import sys
import os
import termios

import random
import string
import re

class BookReader(object):

    """BookReader"""

    """
    Book Reader

    You have some text files. They represent a book. Our book contains chapters. Each chapter starts with # at the beginning of the line. (Markdown book)

    Our book is made of many files. Each file has its number 001.txt, 002.txt, 003.txt

    Each file may contain one or more chapters.

    Write a program that displays on the console each chapter. You can only move forwards using the space button.

    Try not to load the whole book in the memory. Use generator!
    """

    CHAPTER_RE = r'#\s+?Chapter\s+\d+'

    def __init__(self, path='book'):

        self.__path = path
        self.__c_re = re.compile(self.CHAPTER_RE)

    def __read_file(self, path):

        with open(path) as fd:

            for line in fd:

                if self.__c_re.match(line):

                    space_key = self.__wait_space_key()
                    if space_key is False:
                        return

                yield line

        fd.close()

    def __read_path(self):

        for root, _, files in os.walk(self.__path):

            files.sort()

            for fname in files:

                path = '{}/{}'.format(root, fname)

                yield path


    def __wait_space_key(self):

        """ Wait for a space key press on the console and return it. """

        file_fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(file_fd)
        newattr = termios.tcgetattr(file_fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(file_fd, termios.TCSANOW, newattr)

        try:

            result = sys.stdin.read(1)
            result = True if result == ' '  else False

        except IOError:
            pass

        finally:
            termios.tcsetattr(file_fd, termios.TCSAFLUSH, oldterm)

        return result


    def read(self):

        for book_file in self.__read_path():

            for line in self.__read_file(book_file):

                print(line, end='')





class BookGenerator(object):
    """BookGenerator"""

    """
    Make a python program that generates books.

    Your program should take the following parameters.

    Chapters count
    Chapter length range (in words)
    The words should be with random length and random char. 
    The format of the book should be: chapters with paragraphs with sentenses with punctuation. 
    Try to place some new lines in the chapters at random positions. 
    Title and numerate the chapters. 
    The whole book must be in one file.

    Try to generate bigger book. Like 1-2G, and try to pass it to the previous program.
    """

    WORD_LENGTH_RANGE = (6, 9)
    WORDS_PER_SENTENCE_RANGE = (9, 13)
    SENTENCES_PER_PARAGRAPH_RANGE = (3, 4)

    def __init__(self, chapters_count: int, chapter_words_range: tuple) -> None:

        self.__chapters_count = chapters_count
        self.__w_start, self.__w_stop = chapter_words_range

        self.__words_per_chapter = None
        self.__chapter_id = None

        self.__alphabet = list(string.ascii_lowercase) * 1024 
        random.shuffle(self.__alphabet)


    def __generate_word(self) -> str:

        range_start, range_stop = self.WORD_LENGTH_RANGE
        length = random.randrange(range_start, range_stop)

        word = ''.join(random.sample(self.__alphabet, length)) 

        self.__words_per_chapter -= 1

        return word



    def __generate_words(self, amount: int) -> None:


        if self.__words_per_chapter == 0:
            return

        for __ in range(amount):

            yield self.__generate_word()

            if self.__words_per_chapter == 0:
                break


    def __generate_sentence(self) -> str:

        range_start, range_stop = self.WORDS_PER_SENTENCE_RANGE
        words_per_sentence = random.randrange(range_start, range_stop)

        sentence = ' '.join(self.__generate_words(words_per_sentence))

        if(len(sentence) > 0):
            sentence = sentence.capitalize() + '.'

        return sentence

    def __generate_sentences(self, amount: int) -> None:

        for __ in range(amount):

            yield self.__generate_sentence()


    def __generate_paragraph(self) -> str:

        range_start, range_stop = self.SENTENCES_PER_PARAGRAPH_RANGE
        sentances_per_paragraph = random.randrange(range_start, range_stop)

        paragraph = ' '.join(self.__generate_sentences(sentances_per_paragraph))

        return paragraph

    def __generate_paragraphs(self, amount: int) -> None:

        for __ in range(amount):

            yield self.__generate_paragraph()


    def generate(self) -> None:

        with open('books/generated_book.txt', 'w+') as fd:

            for c_count in range(self.__chapters_count):

                self.__chapter_id = c_count + 1
                self.__words_per_chapter = random.randrange(self.__w_start, self.__w_stop)

                paragraphs_per_chapter = random.randrange(2, 4)

                fd.write('# Chapter {}\n\n'.format(self.__chapter_id))

                for paragraph in self.__generate_paragraphs(paragraphs_per_chapter):

                    fd.write('{}\n'.format(paragraph))

        fd.close()
