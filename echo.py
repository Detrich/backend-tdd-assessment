#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Detrich"


import sys
import argparse


def toUppercase(text):
    return text.upper()


def toLowercase(text):
    return text.lower()


def toTitlecase(text):
    return text.title()


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(description="Perform transformation on input text.")
    parser.add_argument('text', help='text to be manipulated')
    parser.add_argument('-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument('-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument('-t', '--title', help='convert text to titlecase', action='store_true')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)
    if not ns:
        parser.print_usage()
        sys.exit(1)
    text = ns.text
    toUpper = ns.upper
    toLower = ns.lower
    toTitle = ns.title
    if text is sys.argv[1]:
        print(text)
    if toTitle:
        print(toTitlecase(text))
    elif toLower:
        print(toLowercase(text))
    elif toUpper:
        print(toUppercase(text))


if __name__ == '__main__':
    main(sys.argv[1:])
