import json
import requests
from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
class Health(Resource):
    def get(self):
        return {"status": "ok"}
class DiagCheck(Resource):
    def get(self):
        response = requests.get("https://www.travel-advisory.info/api")
        return {"api_status": response.json()}
class Convert(Resource):
    def post(self):
        data = request.get_json()
        country_names = data.get("country_names")
        if not country_names:
            return {"error": "Missing country names"}
        country_codes = lookup_country(country_names)
        return {"country_codes": country_codes}
api.add_resource(Health, "/health")
api.add_resource(DiagCheck, "/diag_check")
api.add_resource(Convert, "/convert")
if __name__ == "__main__":
    app.run(debug=True)

