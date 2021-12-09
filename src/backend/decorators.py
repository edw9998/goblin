from functools import wraps

def auth_required(func):
  @wraps(func)
  def decorated(*args, **kwargs):
    # TODO: This part tomorrow
    # jklaf;dsjkl;dasjkl;fdsa
    pass
  return decorated