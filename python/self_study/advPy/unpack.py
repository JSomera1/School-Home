kwargs = {}

# finding if 
if difficulty in ("easy", "medium", "hard"):
    kwargs["difficulty"] = difficulty

if category in get_categories():
    kwargs["category"] = category

if number.isdigit():
    kwargs["number"] = int(number)
    
get_questions(**kwargs)