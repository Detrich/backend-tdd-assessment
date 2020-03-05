#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess


class TestEcho(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(echo.toUppercase("hello!"), "HELLO!")
        self.assertEqual(echo.toUppercase('"hola"'), '"HOLA"')

    def test_lower(self):
        self.assertEqual(echo.toLowercase("HELLO"), "hello")
        self.assertEqual(echo.toLowercase('"HoLA"'), '"hola"')

    def test_title(self):
        self.assertEqual(echo.toTitlecase("hello"), "Hello")
        self.assertEqual(echo.toTitlecase('"hola"'), '"Hola"')
    
    def test_text(self):
        self.assertEqual(("hello"), "hello")

    def test_help(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)


if __name__ == '__main__':
    unittest.main()
