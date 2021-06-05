import wikipedia
def send_summary(msg):
  try:
    return wikipedia.summary(msg,sentences=2)
  except:
    return "Sorry, I cant help you with that :("