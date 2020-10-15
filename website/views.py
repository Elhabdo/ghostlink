from django.shortcuts import render, redirect
from django.http import HttpRequest
import requests
import json as simplejson

#_MYHOST = "http://127.0.0.1:8000/"


_MYHOST = "http://www.ghostlnk.ga/"
# Create your views here.



def home(req):
    return render(req, "index.html", {})


def posst(req):
    url = req.POST["long_url"]
    url_f = shortcut(url)
    data = {
        "url": url_f[0],
        "msg" : url_f[1]
    }
    return render(req, "shorted.html", data)


def shortcut(url: str):
    if not url.startswith("https://") or not url.startswith("https://"):
        url = "https://" + url
    response = requests.get('https://ulvis.net/API/write/get?url='+ url)
    response_json = simplejson.loads(response.text)
    if "data" in response_json:
        data = response_json["data"]
        url_s = data["url"].split("/")[3]
        print(url_s)
        print(response_json)
        url_f = _MYHOST+url_s
        msg = "Your shorted url is ready"
    else:
        url_f = 'url invalide'.upper()
        msg = "Your shorted url is not ready"
    res = (url_f,msg)
    print(res)
    return res

def open(req):
    if req.method == "GET":
        s_url = req.build_absolute_uri()
        sub_url = s_url.split("/")[3]

        l_url = longurl(sub_url)
        if l_url == None:
            return render(req, "404.html", {})
        else:
            return redirect(l_url)
    else:
        pass


def longurl(url):
    reqq = requests.get("https://ulvis.net/API/read/get?id=" + url)
    reqq_json = simplejson.loads(reqq.text)
    print(reqq_json)
    if "data" in reqq_json:
        data = reqq_json["data"]
        url_l = data["full"]
        print(url_l)
        return url_l
