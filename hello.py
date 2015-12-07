#!/usr/bin/env python
# -*- coding: utf-8 -*- 

""" 
   hello.py -- prints friendly, customizable greeting
   Copyright 2015 - Diego Codevilla - <dcodevilla@pioix.edu.ar>
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  
"""

import argparse
import sys

import os
import gettext
import locale

# Names, version, year, URLs used in help and version
PACKAGE_NAME = "GNU Hello"
PACKAGE = "hello"
PROGRAM_NAME = "hello"

VERSION = "2.10"
COPYRIGHT_YEAR = 2014

PACKAGE_BUGREPORT = "bug-hello@gnu.org"
PACKAGE_URL = "<http://www.gnu.org/software/hello/>"

def print_help():
    """ Print help info.  This long message is split into
        several pieces to help translators be able to align different
        blocks and identify the various pieces.  """
        
    print ( _("Usage: %s [OPTION]...") ) % (PROGRAM_NAME)

    print _("Print a friendly, customizable greeting.");
    print ""
   
    print _("  -h, --help          display this help and exit")
    print _("  -v, --version       display version information and exit")

    print ""
  
    print _("  -t, --traditional       use traditional greeting")
    print _("  -g, --greeting=TEXT     use TEXT as the greeting message")

    print ""
    
    print ( _("Report bugs to: %s") ) % PACKAGE_BUGREPORT
    
    print ( _("%s home page: <%s>") ) % (PACKAGE_NAME, PACKAGE_URL);
  
    print _("General help using GNU software: <http://www.gnu.org/gethelp/>")
    


def print_version():
    """ Print version and copyright information. """
    
    print ("%s (%s) %s\n")% (PACKAGE, PACKAGE_NAME, VERSION)
    print ""

    # It is important to separate the year from the rest of the message,
    # as done here, to avoid having to retranslate the message when a new
    # year comes around.  
    print ( _("""Copyright (C) %d Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.\n""") ) % COPYRIGHT_YEAR


def sayHello(args):
    # set internalización configuration to use
    locale.setlocale(locale.LC_ALL, "");
    
    # get localizations' folder
    localedir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'locale'))

    # set tanslation file name (.mo)
    gettext.bindtextdomain('hello', localedir)
    gettext.textdomain('hello')  

    # set default greeting message 
    greeting_msg = _("Hello, world!")

    # if --help / -h print help and exit
    if args.help:
	print_help()
	sys.exit(0)
	
    # if --version / -v print version information and exit
    elif args.version:
	print_version()
	sys.exit(0)
	
    else:
        # if --traditional / -t ...
	if args.traditional:
	    # set greeting message to old-style one
	    greeting_msg = _("hello, world")
	
	# if --greeting / -g ...
	elif args.message:
	    # set greeting message to the string specified
	    greeting_msg = args.message

    # print greeting message and exit
    print greeting_msg
    sys.exit(0)


if __name__ == '__main__':
    # this makes possible to use _() for mark translatable strings
    _ = gettext.gettext
    
     # create argparse object - set automatic help to false
    parser = argparse.ArgumentParser(add_help=False)
    
    # add arguments to parse 
    parser.add_argument("-h", "--help", action="store_true")
    parser.add_argument("-t", "--traditional", help=_(""),action="store_true")
    parser.add_argument("-v", "--version", help=_(""),action="store_true")
    parser.add_argument("-g", "--greeting", help=_(""),action="store", dest="message")

    # parse arguments
    args = parser.parse_args()
    
    sayHello(args)

