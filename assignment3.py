#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 3 Module"""

import urllib2
import csv
import argparse
import re

def downloadData(url):
    """Accomplishes Objective 1: Pull Down Web Log File"""
    data = urllib2.urlopen(url)
    read = csv.reader(data)
    return read

def processData(read):
    hits = 0
    img = 0
    firefox = 0
    chrome = 0
    ie = 0
    safari = 0

    for i in read:
        hits += 1
        if re.search('([.jpg]|[.jpeg]|[.png]|[.gif]|[.JPG]|[.JPEG]|[.PNG]|[.GIF])', i[0]):
            img += 1
        if re.search("firefox", i[2]):
            firefox += 1
        if re.search("chrome", i[2]):
            chrome += 1
        if re.search("ie", i[2]):
            ie += 1
        if re.search("safari", i[2]):
            safari += 1

    imgpct = (float(img) / hits) * 100
    browsers = {'Firefox': firefox, 'Chrome': chrome, 'Internet Explorer': ie, 'Safari': safari}
    popbrowser = max(browsers.values())
    firefoxpct = (float(firefox) / hits) * 100
    chromepct = (float(chrome) / hits) * 100
    iepct = (float(ie) / hits) * 100
    safaripct = (float(safari) / hits) * 100
    print 'The total number of requests for today is:' + str(hits)
    print 'Image requests account for {0:0.1f}% of all requests'.format(imgpct)
    print 'The most popular browser today is:' + str([k for k, v in browsers.iteritems() if v == popbrowser])
    print 'Firefox accounts for {0:0.1f}% of all requests'.format(firefoxpct)
    print 'Chrome accounts for {0:0.1f}% of all requests'.format(chromepct)
    print 'Internet Explorer accounts for {0:0.1f}% of all requests'.format(iepct)
    print 'Safari accounts for {0:0.1f}% of all requests'.format(safaripct)


def main():
    """Main function """
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="Enter the URL to get the CSV file.")
    args = parser.parse_args()

    if args.url:
        try:
            csvData = downloadData(args.url)
            processData(csvData)

        except urllib2.URLError as URLError:
            print "This URL entered is invalid."
            raise URLError
    else:
        print "Please enter a valid URL."

if __name__ == "__main__":
    main()