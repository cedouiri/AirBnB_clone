#!/usr/bin/python3
"""
Unit Test for filestorage
"""
import unittest
import models
import os
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Tests the file storage
    """
    def setUp(self):
        """
        Setup
        """
        self.ikea = FileStorage()

    def tear_down(self):
        """
        tear down
        """
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except BaseException:
                pass

    def test_file_storage(self):
        """
        test for filestorage
        """
        self.assertFalse(hasattr(self.ikea, "fake_id"))


class TestDocumentation(unittest.TestCase):
    """
    class to test documentation
    """

    def test_doc_class(self):
        """
        test class
        """
        expected = ' filestorage class '
        actual = FileStorage.__doc__
        self.assertEqual(expected, actual)

    def test_all(self):
        """
        test all function
        """
        expected = ' defining all '
        actual = FileStorage.all.__doc__
        self.assertEqual(expected, actual)

    def test_new(self):
        """
        test new function
        """
        expected = ' defining new '
        actual = FileStorage.new.__doc__
        self.assertEqual(expected, actual)

    def test_save(self):
        """
        test class
        """
        expected = ' defining save '
        actual = FileStorage.save.__doc__
        self.assertEqual(expected, actual)

    def test_reload(self):
        """
        test reload function
        """
        expected = ' defining reload '
        actual = FileStorage.reload.__doc__
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
