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