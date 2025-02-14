from lib.to_do import Todo
import pytest

"""
test instance of ToDo initialises with correct task property
"""

def test_todo_instance_initialises_with_task_string():
    to_do = Todo('walk dog')
    assert to_do.get_task() == 'walk dog'

"""
test get_task returns the task string
"""

def test_get_task_returns_the_task_string():
    to_do = Todo('walk dog')
    assert to_do.get_task() == 'walk dog'

"""
test instance of ToDo initialises with complete attribute set to False
"""

def test_ToDo_instance_initialises_with_task_complete_set_to_false():
    to_do = Todo('walk dog')
    assert to_do.get_complete() == False

"""
test get_complete returns the status of task completion True/False
"""

def test_get_complete_returns_bool_representing_task_completion_status():
    to_do = Todo('walk dog')
    assert to_do.get_complete() == False

"""
test mark_complete updates the complete property of task to True
"""

def test_mark_complete_updates_complete_attribute_to_True():
    to_do = Todo('walk dog')
    to_do.mark_complete() 
    assert to_do.get_complete() == True

# errors/edgecases

"""
test todo raises err if passed empty str as task
"""

def test_todo_raises_err_if_passed_empty_str():
    with pytest.raises(ValueError) as err:
        to_do = Todo('')
    err_msg = str(err.value)
    assert err_msg == 'task cannot be empty'

"""
test todo raises err if input task not a str
"""
def test_todo_raises_error_for_non_string_task():
    with pytest.raises(TypeError) as err:
        to_do = Todo(7)
    err_msg = str(err.value)
    assert err_msg == 'task must be type string'