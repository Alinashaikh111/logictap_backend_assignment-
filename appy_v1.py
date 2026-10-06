from flask import Flask, request, jsonify

app = Flask(__name__)

calls = {}

@app.route("/call-ended", methods=["POST"])
def call_ended():
    data = request.get_json()

    call_id = data.get("call_id")
    status = data.get("status")
    duration_secs = data.get("duration_secs")

    if not call_id:
        return jsonify({"error": "call_id is required"}), 400

    calls[call_id] = {
        "call_id": call_id,
        "status": status,
        "duration_secs": duration_secs
    }

    return jsonify({"message": "Call stored successfully"}), 200


@app.route("/calls/<call_id>", methods=["GET"])
def get_call(call_id):
    if call_id not in calls:
        return jsonify({"error": "Call not found"}), 404

    return jsonify(calls[call_id]), 200


if __name__ == "__main__":
    app.run(debug=True)