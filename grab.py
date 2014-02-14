#!/usr/bin/env python
__author__ = 'toly'
"""
    Python script (work only in Mac OS) for grabbing books
    from Amazon Kindle, Google Play and other books services
"""

import sys
import argparse


def main():
    """main function"""
    pass


def create_argument_parser():
    """make ArgumentParser object with necesary options"""
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-p", "--output-pdf", type=str, help="file for result output pdf file (*.pdf)")
    argument_parser.add_argument("-t", "--output-txt", type=str, help="file for result output text file (*.txt)")
    argument_parser.add_argument("-n", "--number-pages", type=int, help="number pages for grab (default 1000)")
    argument_parser.add_argument("-c", "--cmp-after", type=int, help="number of pages, after which the last two pages "
                                                                     "will be compared and if they equal - stop")
    return argument_parser


def grabbing_screen(number_pages=None, cmp_pages_after=None):
    """
        grabbing screen, paging and yield images

            number_pages - count pages for grabbing
            cmp_images_after - after that count pages current page and previous page will be compared,
                                and if they will be equal function stoped
    """
    pass


def recognize_image(image):
    """recocginze image and return text"""
    pass


if __name__ == '__main__':
    sys.exit(main())