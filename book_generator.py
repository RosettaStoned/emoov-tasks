#!/usr/bin/env python3                                                          
                                                                                
""" A generator for random books"""                                             
from src.book import BookGenerator                                             
                                                                                
if __name__ == '__main__':                                                      
    BOOKS = BookGenerator(10, (10, 33)).generate()
