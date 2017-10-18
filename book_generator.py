#!/usr/bin/env python3

""" A generator for random books"""
from src.book import BookGenerator

if __name__ == '__main__':
    bg = BookGenerator(10, (10, 33))
    bg.generate()
