from random import random
from typing import List

from pystreamapi import Stream


def main():
    print('main')


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def get_random():
    return random()


def sort_data(array):
    return Stream.of(array) \
        .filter(lambda x: x is not None) \
        .sorted() \
        .to_list()


if __name__ == '__main__':
    main()
