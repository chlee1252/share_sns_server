from flask import request

def getOS():
  userOS = request.user_agent.platform
  if userOS == 'ipad' or userOS == 'iphone':
    return 'iOS'
  elif userOS == 'andorid':
    return 'android'
  else:
    return 'others'