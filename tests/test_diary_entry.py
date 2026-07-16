import pytest
from lib.diary_entry import *

def test_title_of_diary():
    new_entry = DiaryEntry("May the 4th", "today i saw a ballon")
    assert new_entry.title == "May the 4th"

def test_contents_of_diary():
    new_entry = DiaryEntry("May the 4th", "today i saw a ballon")
    assert new_entry.contents == "today i saw a ballon"

def test_new_long_words():
    new_entry = DiaryEntry("on the elventh day of the 10th month", "i frolicked among the tulips and had a whale of a time")
    assert new_entry.count_words() == 12