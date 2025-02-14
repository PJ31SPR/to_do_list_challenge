from lib.to_do_list import TodoList
from unittest.mock import Mock
import pytest

"""
test TodoList initialises with an empty list of todos
"""
def test_todolist_initialises_with_empty_todo_list():
    todo_list = TodoList()
    assert todo_list.get_todos() == []

"""
test add successfully appends a task to the list
"""
def test_add_todo_adds_to_list():
    todo_list = TodoList()
    mock_todo = Mock()  
    todo_list.add(mock_todo)

    assert todo_list.get_todos() == [mock_todo] 

"""
test incomplete returns a list of only incomplete tasks
"""

def test_incomplete_returns_a_list_of_incomplete_tasks():
    todo_list = TodoList()
    mock_todo_1 = Mock()
    mock_todo_1.complete = False
    mock_todo_2 = Mock()
    mock_todo_2.complete = True
    todo_list.add(mock_todo_1)
    todo_list.add(mock_todo_2)
    
    assert todo_list.incomplete() == [mock_todo_1]

"""
test incomplete returns empty list if no todos are incomplete
"""
def test_incomplete_returns_empty_list_when_no_incomplete_todos():
    todo_list = TodoList()
    mock_todo = Mock()
    mock_todo.complete = True
    todo_list.add(mock_todo)
    
    assert todo_list.incomplete() == []

"""
test complete returns a list of only completed tasks
"""

def test_complete_returns_a_list_of_complete_tasks():
    todo_list = TodoList()
    mock_todo_1 = Mock()
    mock_todo_1.complete = False
    mock_todo_2 = Mock()
    mock_todo_2.complete = True
    todo_list.add(mock_todo_1)
    todo_list.add(mock_todo_2)
    
    assert todo_list.complete() == [mock_todo_2]


"""
test complete returns empty list if no todos are complete
"""
def test_complete_returns_empty_list_when_no_complete_todos():
    todo_list = TodoList()
    mock_todo = Mock()
    mock_todo.complete = False
    todo_list.add(mock_todo)
    
    assert todo_list.complete() == []

"""
test give_up updates all todos to completed
"""

def test_give_up_updates_status_of_all_todos_in_list_to_complete():
    todo_list = TodoList()
    todo_list = TodoList()
    mock_todo_1 = Mock()
    mock_todo_1.complete = False
    mock_todo_2 = Mock()
    mock_todo_2.complete = True
    todo_list.add(mock_todo_1)
    todo_list.add(mock_todo_2)

    todo_list.give_up()

    assert todo_list.complete() == [mock_todo_1, mock_todo_2]

    # errors/edgecases

"""
test add raises error if todo is already in list
"""
def test_add_raises_error_if_todo_already_in_list():
    todo_list = TodoList()
    mock_todo = Mock()
    todo_list.add(mock_todo)

    with pytest.raises(ValueError) as err:
        todo_list.add(mock_todo)
    assert str(err.value) == 'todo already exists in list'

# """
# test add raises error if argument passed is not a todo instance
# """
# def test_add_raises_error_if_not_todo_instance():
#     todo_list = TodoList()
#     not_a_todo = "walk dog"
    
#     with pytest.raises(TypeError) as err:
#         todo_list.add(not_a_todo)
#     assert str(err.value) == 'can only add todo instances to list'