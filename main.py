def do_stuff(num=0):
    # num=0, can't fix None
  try:  
    if num:
      return int(num) + 5
    else:
      return "Please enter number"
    # if/else to fix None  
  except ValueError as err:
      return err