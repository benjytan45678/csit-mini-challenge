from flask import Flask

from app.router import flight_api_v1


if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(flight_api_v1)

    @app.route("/")
    def greet():
        return {"message": "Flask app is running!"}

    app.run(debug=True, port=8080)
