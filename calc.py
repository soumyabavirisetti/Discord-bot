def compute(s):
  try:
    return eval(s)
  except:
    return "For "+s+" Evaluation not possible"