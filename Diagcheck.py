from flask_restful import Resource
import requests
import json
class DiagCheck(Resource):
    def get(self):
        response = requests.get("https://www.travel-advisory.info/api")
        data = response.json()
        return data
