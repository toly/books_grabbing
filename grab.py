#!/usr/bin/env python
__author__ = 'toly'
"""
    Python script (work only in Mac OS) for grabbing books
    from Amazon Kindle, Google Play and other books services
"""

import os
import sys
import time
import filecmp
import argparse


def main():
    """main function"""

    # parse arguments
    parser = create_argument_parser()
    args = parser.parse_args()

    # make new tmp dir
    tmp_dir = '/tmp/%s/' % args.title
    if os.path.exists(tmp_dir):
        n = 0
        while os.path.exists(tmp_dir):
            n += 1
            tmp_dir = '/tmp/%s%d/' % (args.title, n)
    os.mkdir(tmp_dir)

    page_images = grabbing_screen(tmp_dir, number_pages=args.number_pages, cmp_pages_after=args.cmp_after)
    for page_number, page_image in enumerate(page_images):
        if 'txt' in args.formats:
            os.system('tesseract %s /tmp/out' % page_image)
            os.system('more "===page #%d" >> %s.txt' % (page_number, args.title))
            os.system('more /tmp/out.txt >> %s.txt' % args.title)

    if 'pdf' in args.formats:
        os.system("convert %spage*.png %s.pdf" % (tmp_dir, args.title))

    os.system("rm -rf %s" % tmp_dir)
    os.system("rm -f /tmp/out.txt")

    print 'Book grabbed'


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


def grabbing_screen(tmp_dir, number_pages=None, cmp_pages_after=None):
    """
        grabbing screen, paging and yield images

            number_pages - count pages for grabbing
            cmp_images_after - after that count pages current page and previous page will be compared,
                                and if they will be equal function stoped
    """
    from pymouse import PyMouse

    m = PyMouse()
    grab_coords = []

    raw_input("Set mouse to up left corner and press enter...")
    grab_coords += list(m.position())

    raw_input("Set mouse to down left corner and press enter...")
    grab_coords += list(m.position())

    grab_coords[2] -= grab_coords[0]
    grab_coords[3] -= grab_coords[1]

    grab_coords = map(lambda x: str(int(x)), grab_coords)

    raw_input("Set mouse to position for paging and press enter")
    paging_coords_args = list(m.position()) + [1]

    def make_screenshot(coords, filename):
        command = "screencapture -R%s %s" % (','.join(coords), filename)
        os.system(command)

    for i in xrange(number_pages):
        current_page_image = image_page(tmp_dir, i)

        make_screenshot(grab_coords, current_page_image)
        m.click(*paging_coords_args)
        time.sleep(1)

        if not i % 10:
            print 'grabing page #%d' % i

        if i > cmp_pages_after:
            prev_image = image_page(tmp_dir, i - 1)
            if filecmp.cmp(current_page_image, prev_image):
                os.system("rm %s" % current_page_image)
                break

        yield current_page_image


def image_page(pages_dir, page_number):
    """generate name page image by number and tmp dir"""
    return os.path.join(pages_dir, 'page%04d.png' % page_number)


if __name__ == '__main__':
    sys.exit(main())