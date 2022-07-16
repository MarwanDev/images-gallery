from urllib import response
import requests 
from flask import Flask, request

UNSPLASH_URL="https://api.unsplash.com/photos/random"
UNSPLASH_KEY="t11X0zZNEoDJNqc7e3M0Uj3RIV37FQAzf5g9yhk9k8U"

app = Flask(__name__)

@app.route("/new-image")
def new_image():
   word = request.args.get("query")
   headers={
    "Accept-Version":"v1",
    "Authorization":"Client-ID " + UNSPLASH_KEY
   }
   params = {
    "query":word
   }
   response = requests.get(UNSPLASH_URL, headers=headers, params=params)
   data=response.json()
   return {"data":data} 

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5050)