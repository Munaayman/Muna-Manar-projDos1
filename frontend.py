from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd
import requests

app = Flask(__name__)
api = Api(app)
       
class Info(Resource):

    def get(self,num):
        #to catalog server
        #search by id
        return requests.get('http://172.19.221.41:5000/info/'+str(num)).json()
  
api.add_resource(Info, '/info/<int:num>')


if __name__ == '__main__':
    app.run()
    #manar