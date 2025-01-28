from unittest.mock import Mock, patch, mock_open
import builtins

def add_two_numbers():
    num1 = int(input("enter first number? "))
    num2 = int(input("enter second number? "))
    return num1 + num2

#ver 1 
def test_add_two_numbers():
    #failing test because it depends on the user input 
    with patch("builtins.input", return_value="10") as mock_input:
        assert add_two_numbers() == 20
        assert mock_input.call_count == 2

#ver 2  
@patch("builtins.input", return_value="10") #you can use side_effect = [values]
def test_add_two_numbers(mock_input):
    assert add_two_numbers() == 20
    assert mock_input.call_count == 2



m = Mock() #object that will never complain about anything 
m2 = Mock(side_effect=["1","2","3","4","5","6"])

#use patch using a 'with' block
# patch creates a mock objecdt using arguements in patch call
# builtins.input == input

# dealing with pathing random in code  
#  
def first_line():
    with open("words.txt") as file:
        return file.readline().strip()
    
#@patch("builtins.open", new_callable = mock_open, read_data="Something\nbob") <- last part allows writing information for test if file does not exist
# def test_first_line(mock_file):
#   assert first_line() == "Tim"