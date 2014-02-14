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

    parser = create_argument_parser()
    arguments = parser.parse_args()

    try:
        validate_args(arguments)
    except GrabException as e:
        print "Error: %s!" % e.message
        print "For help run: ./grap.py -h"
        return 1


def create_argument_parser():
    """make ArgumentParser object with necesary options"""
    argument_parser = argparse.ArgumentParser()

    argument_parser.add_argument("-t", "--title", type=str, required=True, help="book title")
    argument_parser.add_argument("-f", "--formats", type=str, required=True, nargs="*",
                                 help="need formats of output file", choices=["pdf", "txt"])
    argument_parser.add_argument("-n", "--number-pages", type=int, help="number pages for grab (default 1000)",
                                 default=1000)

    help_for_cmp_after = "number of pages, after which the last two pages will be compared and if they equal - stop"
    argument_parser.add_argument("-c", "--cmp-after", type=int, help=help_for_cmp_after, default=3)

    return argument_parser


class GrabException(Exception):
    pass


def validate_args(args):
    """validate command line rguments"""

    raise GrabException('zzz')


def grabbing_screen(number_pages=None, cmp_pages_after=None):
    """
        grabbing screen, paging and yield images

            number_pages - count pages for grabbing
            cmp_images_after - after that count pages current page and previous page will be compared,
                                and if they will be equal function stoped
    """
    pass


def recognize_image(image):
    """recoginze image and return text"""
    pass


if __name__ == '__main__':
    sys.exit(main())