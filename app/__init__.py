from sanic import Sanic

from app.config import get_config_obj

session = {}


def create_app():
    app = Sanic(__name__)
    config_obj = get_config_obj()
    app.config.from_object(config_obj)

    from app.view.user_blueprint import user_blueprint
    from app.view.view_blueprint import view_blueprint
    app.blueprint(user_blueprint)
    app.blueprint(view_blueprint)

    @app.middleware('request')
    async def add_session_to_request(request):
        request['session'] = session

    return app
