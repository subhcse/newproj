from flask_restful import Resource
import json
class Convert(Resource):
    def post(self):
        data = request.get_json()
        country_names = data["country_names"]
        country_codes = lookup_country(country_names)
        return {"country_codes": country_codes}
def lookup_country(country_names):
    with open("data.json", "r") as f:
        data = json.load(f)
    result = {}
    for country_name in country_names:
        for country_code, name in data.items():
            if name.lower() == country_name.lower():
                result[country_name] = country_code
                break
    return result
