from flask import Flask

from app.router import flights_api_v1, hotels_api_v1


if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(flights_api_v1)
    app.register_blueprint(hotels_api_v1)

    @app.route("/")
    def greet():
        return {"message": "Flask app is running!"}

    app.run(debug=True, port=8080)
