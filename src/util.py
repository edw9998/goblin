def validate_input(qmsg, checkf, emsg="Input error!"):
  """
  qmsg: question message
  checkf: check function
  emsg: error message
  """
  while True:
    print(qmsg)
    msg = input()
    if (checkf(msg)):
      return msg
    else:
      print(emsg)
      
def check_name(msg):
  # Check whitespace
  for x in msg:
    if x == " ":
      return False
 
  # Less than 20 characters 
  if len(msg) > 20 or len(msg) < 3:
    return False
  
  return True

def check_password(msg):
  # Less than 30 characters 
  if len(msg) > 30 or len(msg) < 5:
    return False
  
  number_there = False
  # Check number
  for x in msg:
    if x.isnumeric():
      number_there = True
      
  return number_there