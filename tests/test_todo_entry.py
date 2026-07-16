from lib.todo_entry import *

def test_to_entry_can_be_made():
    new_todo = Todo_Entry("walk the dog")
    assert new_todo.task == "walk the dog"
