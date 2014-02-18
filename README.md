books_grabbing
==============

Python script for grabbing (and optional recognize) books from Amazon, Google Play, etc.

P.S. Now, script work only on Mac OS.

## How to use

[http://www.youtube.com/watch?v=BUBLhS6gu6E](http://www.youtube.com/watch?v=BUBLhS6gu6E)

## Install requirements

    $ brew install imagemagick
    $ brew install tesseract
    $ pip install pyobjc-core
    $ pip install pyobjc
    $ pip install pymouse

## Usage

    $ ./grab.py -h
    usage: grab.py [-h] -t TITLE -f [{pdf,txt} [{pdf,txt} ...]] [-n NUMBER_PAGES]
                   [-c CMP_AFTER]

    optional arguments:
      -h, --help            show this help message and exit
      -t TITLE, --title TITLE
                            book title
      -f [{pdf,txt} [{pdf,txt} ...]], --formats [{pdf,txt} [{pdf,txt} ...]]
                            need formats of output file
      -n NUMBER_PAGES, --number-pages NUMBER_PAGES
                            number pages for grab (default 1000)
      -c CMP_AFTER, --cmp-after CMP_AFTER
                            number of pages, after which the last two pages will
                            be compared and if they equal - stop
