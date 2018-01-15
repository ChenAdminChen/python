from flask import Flask, session

# from flask.json import JSONEncoder
# from datetime import date,timedelta

# defaul flask app config
class DefaultConfig():
    JSON_AS_ASCII = False
    BUNDLE_ERRORS = True

def create_app(config_file):
    app = Flask(__name__)
    app.config.from_object(DefaultConfig)
    app.config.from_pyfile(config_file)

    import mysql_db
    #mysql need app in inject
    mysql_db.mysql.init_app(app)

    from ws_portal import portal
    from ws_restful import ws_restful

    #Blueprints inject
    app.register_blueprint(portal, url_prefix = '/ws-portal')
    app.register_blueprint(ws_restful, url_prefix = '/ws-restful')

    return app

# class CustomJSONEncoder(JSONEncoder):

#     def default(self, obj):
#         try:
#             if isinstance(obj, date):
#                 return obj.strftime('%Y-%m-%d %H:%M:%S')
#             iterable = iter(obj)
#         except TypeError:
#             pass
#         else:
#             return list(iterable)
#         return JSONEncoder.default(self, obj)

if __name__ == '__main__':
    app = create_app('production_config.py')

    # app.json_encoder = CustomJSONEncoder
    app.secret_key = 'UN5yJhqNmLntmHkc'

    app.run(host='0.0.0.0', port=8081)
