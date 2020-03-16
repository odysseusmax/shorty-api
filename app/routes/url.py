from flask.views import MethodView
from flask import request

from app.utils import URLValidator
from app.models import UrlModel


class Url(MethodView):

    def get(self):
        args = request.args
        if not args:
            return {"status": 400, "message":"No code provided."}
        
        code = args.get('code')
        if not code:
            return {"status": 406, "message":"No code provided."}
        
        db = UrlModel()
        if not db.is_an_entry(code):
            return {"status": 404, "message":"Code not found"}
        
        entry = db.get_entry(code)
        data = {
            'code':entry['code'],
            'url': entry['url'],
            'created_on': entry['created_on']
        }
        
        return {"status":200, 'data' : data}
        

    def post(self):
        data = request.form
        if not data:
            return {"status": 400, "message":"No data provided."}
        
        url = data.get('url')
        if not url:
            return {"status": 400, "message":"No url provided."}
        
        valid = URLValidator().is_valid(url)
        if not valid:
            return {"status": 406, "message":"Url provided is not a valid url."}
        
        db = UrlModel()
        entry = db.add_entry(url)
        data = {
            'code':entry['code'],
            'url': entry['url'],
            'created_on': entry['created_on']
        }
        
        return {"status":201, 'data' : data}
