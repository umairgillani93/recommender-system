from flask import Flask
from flask_restful import Resource, Api
from RecPackage import recsys1

app = Flask(__name__)
api = Api(app)

class Recommendations(Resource):
    def get(self):

        myfunc = recsys1.MovieChoice('Young Guns (1988)')
        myfunc = myfunc.to_dict('list')

        return {'Recommedations': myfunc}

api.add_resource(Recommendations, '/')

if __name__ == '__main__':
    app.run(debug = True)