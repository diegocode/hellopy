#!/usr/bin/env python
# -*- coding: utf-8 -*- 

""" 
   hello_tests.py -- tests for hello.py
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

import unittest
import os
import gettext
import locale 
import subprocess

class hello_tests(unittest.TestCase):
	""" Test cases for hello.py
	"""
	
	def testWithoutArguments(self):
	    p = subprocess.Popen(["python hello.py"], 
			  stdout=subprocess.PIPE, 
                          stderr=subprocess.PIPE, shell=True)
	    out, err = p.communicate()
	   			
	    self.assertEqual(out,_("Hello, world!\n"))
		
	def testEnglishOnly(self):
	    p = subprocess.Popen(["python hello.py"], 
			  stdout=subprocess.PIPE, 
                          stderr=subprocess.PIPE, shell=True)
	    out, err = p.communicate()
	   			
	    self.assertNotEqual(out,"Hello, world!\n")	   
			
	def testTraditionalOption(self):
	    p = subprocess.Popen(["python hello.py --traditional"], 
			  stdout=subprocess.PIPE, 
                          stderr=subprocess.PIPE, shell=True)
	    out, err = p.communicate()
	   			
	    self.assertEqual(out,_("hello, world\n"))
				
	def testGreetingOption(self):
	    p = subprocess.Popen(["python hello.py -g 'alfa beta'"], 
			  stdout=subprocess.PIPE, 
                          stderr=subprocess.PIPE, shell=True)
	    out, err = p.communicate()
	   			
	    self.assertEqual(out,"alfa beta\n")	

if __name__ == '__main__':
    # needed to compare translated strings correctly
    locale.setlocale(locale.LC_ALL, "");
    
    # get localizations' folder
    localedir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'locale'))

    # set tanslation file name (.mo)
    gettext.bindtextdomain('hello_tests', localedir)
    gettext.textdomain('hello_tests')  
    _ = gettext.gettext
  
    unittest.main()