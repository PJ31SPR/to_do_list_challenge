from lib.to_do import Todo
from lib.to_do_list import TodoList
import pytest

"""
test can add Todo instances to TodoList and retrieve them
"""
def test_can_add_and_retrieve_todos():
    todo_list = TodoList()
    todo = Todo('walk dog')
    todo_list.add(todo)
    assert todo_list.get_todos() == [todo]
    assert todo_list.get_todos()[0].get_task() == 'walk dog'

"""
test can track completion status of multiple todos
"""
def test_can_track_multiple_todos_completion():
    todo_list = TodoList()
    todo_1 = Todo('walk dog')
    todo_2 = Todo('feed cat')
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    
    todo_1.mark_complete()
    
    assert todo_list.complete() == [todo_1]
    assert todo_list.incomplete() == [todo_2]

"""
test give_up marks all todos as complete
"""
def test_give_up_marks_all_todos_complete():
    todo_list = TodoList()
    todo_1 = Todo('walk dog')
    todo_2 = Todo('feed cat')
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    
    todo_list.give_up()
    
    assert todo_list.complete() == [todo_1, todo_2]
    assert todo_list.incomplete() == []

# errors and edgecases

"""
test cannot add duplicate todos
"""
def test_cannot_add_duplicate_todos():
    todo_list = TodoList()
    todo = Todo('walk dog')
    todo_list.add(todo)
    
    with pytest.raises(ValueError) as err:
        todo_list.add(todo)
    assert str(err.value) == 'todo already exists in list'

"""
test todos with same task but different objects
"""
def test_can_add_todos_with_same_task():
    todo_list = TodoList()
    todo_1 = Todo('walk dog')
    todo_2 = Todo('walk dog')  # Same task, different object
    
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    
    assert len(todo_list.get_todos()) == 2