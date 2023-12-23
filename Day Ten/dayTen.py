def format_name(f_name, l_name):
  """
  Formats the given first name and last name by capitalizing the first letter of each name.
  
  Args:
    f_name (str): The first name.
    l_name (str): The last name.
  
  Returns:
    str: The formatted full name.
    
  Raises:
    None
  """
  if f_name == "" or l_name == "":
    return "You didnt provide a valid input" # Leaves the function if there is an empty string
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"{formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
