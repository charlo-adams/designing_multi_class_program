import pytest
from lib.diary import *
from lib.diary_entry import *
from lib.todo_entry import *
from lib.contact_entry import *

def test_diary_entries_can_be_added():
    my_diary = Diary()
    new_entry = DiaryEntry("May the 4th", "today i saw a ballon")
    my_diary.add_to_diary(new_entry)
    assert my_diary.diary == [new_entry]


def test_todo_entry_can_be_added_to_diary():
    my_diary = Diary()
    new_todo = Todo_Entry("walk the dog")
    my_diary.add_to_todo_list(new_todo)
    assert my_diary.todo_list == [new_todo]

def test_Can_read_diary_entry():
    my_diary = Diary()
    new_entry = DiaryEntry("May the 4th", "today i saw a ballon")
    my_diary.add_to_diary(new_entry)
    new_entry_2 = DiaryEntry("december 21", "i flew into the side of a building")
    my_diary.add_to_diary(new_entry_2)
    assert my_diary.read_diary("May the 4th") ==  "today i saw a ballon"

def test_none_return_when_reading_entry():
    my_diary = Diary()
    new_entry = DiaryEntry("May the 4th", "today i saw a ballon")
    my_diary.add_to_diary(new_entry)
    new_entry_2 = DiaryEntry("december 21", "i flew into the side of a building")
    my_diary.add_to_diary(new_entry_2)
    assert my_diary.read_diary("september 17th") == None


def test_best_entry_for_reading_time_and_minutes():
    my_diary = Diary()
    new_entry_1 = DiaryEntry("what happended", "Today i saw a balloon and it floated away as i ran to it but it was gone so i cried alot")
    new_entry_2 = DiaryEntry("december 21", "i flew into the side")
    my_diary.add_to_diary(new_entry_1)
    my_diary.add_to_diary(new_entry_2)
    assert my_diary.find_best_entry_for_reading_time(2, 3) == new_entry_2

def test_contacts_can_be_added():
    my_diary = Diary()
    new_contact = Contacts("Nikki: 079573957673")
    my_diary.add_to_contacts(new_contact)
    assert my_diary.contact_list == [new_contact]