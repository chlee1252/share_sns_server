import os
from flask import Flask, request, redirect
from src.platform import getOS

app = Flask(__name__)

@app.route('/')
def main():
  return ""

@app.route('/facebook/<account>')
def facebook(account):
  userOS = getOS()
  if userOS == 'iOS':
    return redirect("fb://profile?id={}".format(account), code=307)
  elif userOS == "android":
    return redirect("intent://profile/{}#Intent;package=com.facebook.katana;scheme=fb;end".format(account), code=307)
  else:
    return redirect("https://www.facebook.com/")

@app.route('/snapchat/<account>')
def snapchat(account):
  userOS = getOS()
  if userOS == 'iOS':
    return redirect("snapchat://add/{}".format(account), code=307)
  elif userOS == 'android':
    return redirect("intent://add/{}#Intent;scheme=snapchat;package=com.snapchat.android;end;".format(account), code=307)
  else:
    return 'others'

@app.route('/instagram/<account>')
def instagram(account):
  userOS = getOS()
  if userOS == 'iOS':
    return redirect("instagram://user?username={}".format(account), code=307)
  elif userOS == 'android':
    return redirect("intent://instagram.com/_u/{}/#Intent;package=com.instagram.android;scheme=https;end".format(account), code=307)
  else:
    return 'others'


if __name__=="__main__":
  port = int(os.environ.get('PORT', 5500))
  app.run(debug=True, host='0.0.0.0', port=port)