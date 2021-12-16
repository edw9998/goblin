def validate_input(qmsg, checkf, emsg="Input error!"):
  """This function is used to validate inputs that the user enter. First, it
  asks the question from the `qmsg` string, and then asks for an input. Then,
  the string will be inputted as the parameter for the `checkf` function
  if the `checkf` function returns true, then validate_input will return the
  input string. If the `checkf` function returns false, it will print `emsg`
  and loops back printing the question message.

  Args:
      qmsg (str): "Question Message" This will get printed first to ask the
      input
      checkf (func): Function that is used to validate the input. It has one
      parameter of msg and should return True if the input is valid and false
      if the input is invalid.
      emsg (str, optional): The message that the function prints if the input
      is invalid. Defaults to "Input error!".

  Returns:
      str: The validated string
  """
  while True:
    print(qmsg)
    msg = input()
    if (checkf(msg)):
      return msg
    else:
      print(emsg)
      
def check_name(msg):
  """Checks username. The length should be between 3 and 20 characters, and it
  should not include any whitespaces

  Args:
      msg (str): The message to be validated

  Returns:
      bool: True if the message is valid. False otherwise
  """
  # Check whitespace
  for x in msg:
    if x == " ":
      return False
 
  # Less than 20 characters 
  if len(msg) > 20 or len(msg) < 3:
    return False
  
  return True

def check_password(msg):
  """Checks username. The length should be between 3 and 30 characters, and it
  should include at least one number

  Args:
      msg (str): The message to be validated

  Returns:
      bool: True if the message is valid. False otherwise
  """
  # Less than 30 characters 
  if len(msg) > 30 or len(msg) < 5:
    return False
  
  number_there = False
  # Check number
  for x in msg:
    if x.isnumeric():
      number_there = True
      
  return number_there

def print_sep():
  """Prints a separator
  """
  print("==========================================================")