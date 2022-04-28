import pymongo
from pymongo import MongoClient
from sanic import Sanic, response
from sanic.response import json,html


app=Sanic("onur")

cluster=pymongo.MongoClient("mongodb://mongodb:27017/")
db=cluster["deneme1"]
collection=db["deneme2"]

@app.route("/")
async def test(request):
    return html("""<head><title>Onur Canoğlu</title></head>
    <h1>Onur Canoğlu / DevOps Intern</h1>

    <h3>Welcome to my Docker File</h3>
    <hr>

    <h3 id="idolsun">Lorem.</h3> <!-- h3#idolsun>lorem1 -->
    <ul>
        <li class="id1">Sanic Web Server</li>   <!-- ul>li.id$*3-->
        <li class="id2">Mongodb & Pymongo</li>
        <li class="id3">Dockerize</li>
    </ul> """)


@app.route("/json", methods=['POST'])
def post_json(request):
    post = collection.insert_one(request.json).inserted_id
    return json({"received": True, "Content": str(post)})  


@app.route("/json2", methods=["GET"])
def get_json(response):
    get=list(collection.find(response.json))
    return json({"Content": str(get)})
    
   


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)
