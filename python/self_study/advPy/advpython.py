#Advanced python unpacking iterables and dict 


"""
a function may take variable number of arguments
or when all arguments to a function call are already available in a dictionary list

python uses "unpacking" for these arguments 
*args for iteratable -> arrays are iterable (objects that can be looped over)
**kwargs for dictionary 
"""

#all of 'pos' are positional arguments meaning they match with positions
def func(pos1, pos2, pos3, keyword1="value1", keyword2=None, keyword3=42):
    pass

"""
pos1, 2 and 3 are required and technically do not need the names assigned to them 

## all that matters is that the positions are the same 
func(1,"b",None)

*args is a list of positional arguments
**kwargs is a dictionary of keyword/value arguments/parameters
    - means that position does not really matter 

"""

#exmple of something iterable
def func(*args):
    # the argument with a single * creates a list of passed in values 
    print(args)

func("yes",2) # prints a list of ["yes", 2]


#example of dictionary
def func2(**kwargs):
    print(kwargs)

func2(example="yes", value=2) # prints {"example": "yes", "value":2}


#you can also unpack them
my_list = ["yes", 2]
my_dict = {"example": "yes", "value": 2}

func(*my_list) # equivalent to func("yes", 2)
func(**my_dict) # equivalent to func(example="yes", value=2)

#powerful for dealing with variable/multiple arguments 
kwargs = {}

# finding if 
if difficulty in ("easy", "medium", "hard"):
    kwargs["difficulty"] = difficulty

if category in get_categories():
    kwargs["category"] = category

if number.isdigit():
    kwargs["number"] = int(number)
    
get_questions(**kwargs)