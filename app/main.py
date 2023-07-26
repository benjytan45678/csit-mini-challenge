from flask import Flask
from router import flight_api_v1, hotel_api_v1


if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(flight_api_v1)
    app.register_blueprint(hotel_api_v1)

    @app.route("/")
    def greet():
        return {"message": "Flask app is running!"}

    app.run(debug=True, host="0.0.0.0", port=8080)
