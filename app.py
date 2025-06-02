from flask import Flask, request, jsonify, render_template
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add("Access-Control-Allow-Methods", "POST")
    return response


# Preprocess text: tokenize, remove stopwords and punctuation
def preprocess(text):
    if not text or not isinstance(text, str):
        return []
    try:
        tokens = word_tokenize(text.lower())
        stop_words = set(stopwords.words("english") + list(string.punctuation))
        return [word for word in tokens if word not in stop_words]
    except LookupError:
        # Fallback if NLTK data isn't available
        return text.lower().split()


# Intent matching
def get_intent(user_input):
    processed_input = preprocess(user_input)

    # Define keyword patterns for each intent
    intents = {
        "product_types": ["sell", "products", "types", "kinds", "offer", "carry"],
        "authenticity": ["original", "authentic", "genuine", "real", "fake"],
        "brands": ["international", "local", "brand", "brands", "country"],
        "place_order": ["order", "place", "purchase", "buy", "how"],
        "payment_methods": ["payment", "pay", "methods", "credit", "debit", "cash"],
        "delivery_time": ["delivery", "time", "long", "days", "when", "arrive"],
        "free_shipping": ["free", "shipping", "delivery", "charge"],
        "return_policy": ["return", "exchange", "policy", "send back"],
        "initiate_return": ["initiate", "start", "return", "exchange", "how"],
        "refund_time": ["refund", "money back", "when", "how long", "get back"],
    }

    # Match user input to intent based on keywords
    for intent, keywords in intents.items():
        if any(keyword in processed_input for keyword in keywords):
            return intent

    return None


# Generate response based on intent
def generate_response(intent):
    responses = {
        "product_types": "We offer a wide range of beauty products including makeup (foundations, lipsticks, eyeshadows), skincare (cleansers, moisturizers, serums), haircare (shampoos, conditioners, treatments), and fragrances for both men and women.",
        "authenticity": "All our products are 100% original and authentic, sourced directly from manufacturers or authorized distributors. We guarantee the authenticity of every item in our store.",
        "brands": "We carry both international luxury brands (like MAC, Estée Lauder, Dior) and high-quality local brands that are cruelty-free and vegan.",
        "place_order": "You can place an order through our website by adding items to your cart and proceeding to checkout. For phone orders, please call our customer service at 1-800-BEAUTY.",
        "payment_methods": "We accept all major credit/debit cards (Visa, MasterCard, American Express), PayPal, Apple Pay, Google Pay, and bank transfers. Cash on delivery is also available in select areas.",
        "delivery_time": "Standard delivery takes 3-5 business days. Express delivery (available for an additional fee) delivers within 1-2 business days. Delivery times may vary based on your location.",
        "free_shipping": "Yes! We offer free standard shipping on all orders over $50. For orders below $50, a flat shipping fee of $5 applies.",
        "return_policy": "We accept returns within 30 days of purchase for unopened and unused products with original packaging. Exchanges are subject to product availability.",
        "initiate_return": "To initiate a return, please log in to your account, go to 'My Orders' and select 'Return Item'. Alternatively, you can email returns@beautystore.com with your order number.",
        "refund_time": "Refunds are processed within 3-5 business days after we receive your return. The time it takes for the refund to reflect in your account depends on your payment method (up to 10 business days for credit cards).",
        "default": "I'm here to help with your beauty shopping questions! Could you please rephrase your question? I can tell you about our products, ordering process, payments, delivery, and returns.",
    }

    return responses.get(intent, responses["default"])


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    intent = get_intent(user_message)
    bot_response = generate_response(intent)
    return jsonify({"response": bot_response})


if __name__ == "__main__":
    app.run(debug=True)
