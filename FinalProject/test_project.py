import project
import pytest
from unittest.mock import patch # Simulate user input

# Test add_password function, generate password
@patch('builtins.input', side_effect=['Email', 'user1','y'])
def test_add_password1(mock_input):
    passwords_file = {"accounts": {}}
    project.add_password(passwords_file)
    assert "user1" in passwords_file["accounts"]["Email"]

# Test add_password function, not generate password
@patch('builtins.input', side_effect=['Email', 'user1', 'n', 'pass1'])
def test_add_password2(mock_input):
    passwords_file = {"accounts": {}}
    project.add_password(passwords_file)
    assert "user1" in passwords_file["accounts"]["Email"]
    assert passwords_file["accounts"]["Email"]["user1"]["password"] == "pass1"

# Test update_password function
@patch('builtins.input', side_effect=['Email', 'user1', 'pass2'])
def test_update_password(mock_input):
    passwords_file = {"accounts": {"Email": {"user1": {"password": "pass1"}}}}
    project.update_password(passwords_file)
    assert passwords_file["accounts"]["Email"]["user1"]["password"] != "pass1"
    assert passwords_file["accounts"]["Email"]["user1"]["password"] == "pass2"


# Test delete_password function
@patch('builtins.input', side_effect=['Email', 'user1'])
def test_delete_password(mock_input):
    passwords_file = {"accounts": {"Email": {"user1": {"password": "pass1"}}}}
    project.delete_password(passwords_file)
    assert "user1" not in passwords_file["accounts"]["Email"]
