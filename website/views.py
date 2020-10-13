from django.shortcuts import render,redirect
from django.http import HttpRequest
import requests
import json as simplejson

_MYHOST = "http://www.ghostlnk.ga/"
# Create your views here.

def home(req):
    return render(req, "index.html",{})

def posst(req):
    url = req.POST["long_url"]
    url_f = shortcut(url)
    data = {
        "url" : url_f,
        "old_url" : url
    }
    return render(req,"shorted.html",data)

def shortcut(url:str):
    if not url.startswith("https://") or not url.startswith("https://"):
        url = "https://"+url
    data = {"url": url}
    response = requests.post('https://rel.ink/api/links/', json=data)
    response_json = simplejson.loads(response.text)
    url_short = response_json['hashid']
    url_f = _MYHOST + url_short
    return url_f

def open(req):
    if req.method == "GET":
        s_url = req.build_absolute_uri()
        l_url = longurl(s_url)
        return redirect(l_url)
    else:
        pass

def longurl(url):
    hashid = url.split("/")[3]
    reqq = requests.get("https://rel.ink/api/links/" + hashid)
    reqq_json = simplejson.loads(reqq.text)
    url_long = reqq_json['url']
    return url_long