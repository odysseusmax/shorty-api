from .routes import Home, Url

def register_routes(app):
    app.add_url_rule('/api/v1/url', view_func=Url.as_view('Url'))
    app.add_url_rule('/', view_func=Home.as_view('Home'))
