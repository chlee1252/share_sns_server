import os
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
  return "Hello"

@app.route('/facebook/<account>')
def facebook(account):
  userOS = request.user_agent.platform
  if userOS == "ipad" or userOS == "iphone":
    return redirect("fb://profile?id={}".format(account), code=307)
  elif userOS == "android":
    return "This is andorid"
  else:
    return "This is others"

@app.route('/snapchat')
def snapchat():
  userOS = request.user_agent.platform
  if userOS == "ipad" or userOS == 'iphone':
    return "ios"
  elif userOS == 'android':
    return redirect("intent://instagram.com/p/chlee1127/#Intent;package=com.instagram.android;scheme=https;end", code=307)
  else:
    return 'others'

@app.route('/instagram')
def instagram():
  userOS = request.user_agent.platform
  if userOS == "ipad" or userOS == 'iphone':
    return "ios"
  elif userOS == 'android':
    return 'android'
  else:
    return 'others'


if __name__=="__main__":
  port = int(os.environ.get('PORT', 5500))
  app.run(debug=True, host='0.0.0.0', port=port)