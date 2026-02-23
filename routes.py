from flask import Blueprint, request, jsonify
from .services import generate_podcast_content

main = Blueprint("main", __name__)


@main.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "API is running",
        "message": "AI Podcast Content Assistant Backend Active"
    }), 200


@main.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    if not data or "topic" not in data:
        return jsonify({"error": "Topic is required"}), 400

    topic = data["topic"]

    try:
        result = generate_podcast_content(topic)

        return jsonify({
            "success": True,
            "data": result
        }), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception:
        return jsonify({"error": "Internal Server Error"}), 500