from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

AFFIRMATIONS = [
    "I am worthy of clear and consistent communication.",
    "My feelings are valid, and I deserve to express them.",
    "I trust my intuition about this connection.",
    "I have the strength to define my own needs.",
    "I will not settle for less than I deserve.",
    "I am capable of setting and maintaining healthy boundaries.",
    "I deserve a relationship that feels secure and reciprocal.",
    "I am focused on my own well-being and happiness.",
    "I will speak my truth with kindness and conviction.",
    "I have clarity on what I want and need.",
    "I release the need to label this connection immediately.",
    "I accept the present moment without resistance.",
    "My peace is a top priority.",
    "I attract relationships that honor my worth.",
    "I am patient with myself as I navigate this dynamic.",
    "I am whole and complete on my own.",
    "I deserve to be chosen enthusiastically.",
    "I will act from a place of love, not fear.",
    "I am resilient, and I can handle any outcome.",
    "I respect myself enough to walk away if necessary.",
    "I allow myself to feel all my emotions without judgment.",
    "I am moving forward with intention and grace.",
    "I am grateful for the lessons this situationship is teaching me.",
    "I choose relationships that support my growth.",
    "I honor my boundaries and my energy."
]

def get_random_affirmation():
    affirmation_text = random.choice(AFFIRMATIONS)
    return affirmation_text  # Return just the string, not a dictionary

@app.route("/get-affirmations")
def get_affirmation():
    affirmation_text = get_random_affirmation()  # CALL the function with ()
    affirmations = { "affirmation": affirmation_text }  # Create the dictionary here
    return jsonify(affirmations), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port = port, debug=False)
