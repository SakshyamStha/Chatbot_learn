from django.shortcuts import render
from django.http import JsonResponse
import random

# Sample product data structure
products = {
    "1": {
        "name": "Wireless Headphones",
        "description": "High-quality wireless headphones with noise cancellation.",
        "price": 99.99
    },
    "2": {
        "name": "Smartphone",
        "description": "Latest model smartphone with advanced features.",
        "price": 699.99
    },
    "3": {
        "name": "Laptop",
        "description": "Powerful laptop for gaming and professional use.",
        "price": 1299.99
    },
}

def chatbot_response(request):
    user_message = request.GET.get('message', '').lower().strip()

    responses = {
        "greeting": ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Greetings! How may I help you?"],
        "order": ["Sure! What product would you like to order?", "I can help you with your order. Please tell me what you need."],
        "help": ["I'm here to help! What do you need assistance with?", "Let me know how I can assist you."],
        "thank_you": ["You're welcome! If you have any other questions, feel free to ask."],
        "goodbye": ["Goodbye! Have a great day!", "See you later!"],
        "fallback": ["I'm not sure how to respond to that. Can you please rephrase?"],
    }

    words = user_message.split()

    # Respond to greetings
    if any(word in words for word in ["hello", "hi", "hey"]):
        response = random.choice(responses["greeting"])
    # Check for product inquiries
    elif any(word in words for word in ["product", "details", "info", "tell", "about", "laptop", "smartphone", "wireless"]):
        product_name = extract_product_name(user_message)
        if product_name:
            response = get_product_details(product_name)
        else:
            response = "Sorry, I couldn't find that product. Can you specify which one you mean?"
    # Check for order intent
    elif "order" in words:
        product_name = extract_product_name(user_message)
        if product_name:
            response = place_order(product_name)
        else:
            response = "Sorry, I couldn't find that product to place an order. Can you specify which one you want to order?"
    # Handle help inquiries
    elif any(word in words for word in ["help", "assist"]):
        response = random.choice(responses["help"])
    # Handle thank you and goodbye messages
    elif any(word in words for word in ["thank", "thanks"]):
        response = random.choice(responses["thank_you"])
    elif any(word in words for word in ["bye", "goodbye"]):
        response = random.choice(responses["goodbye"])
    else:
        response = random.choice(responses["fallback"])

    return JsonResponse({"response": response})

def extract_product_name(user_message):
    user_message = user_message.lower()  # Lowercase for case-insensitive matching
    
    # Look for specific product names in the user message
    for product in products.values():
        if product["name"].lower() in user_message:
            return product["name"]

    # Handle common product inquiries
    if "laptop" in user_message:
        return "Laptop"
    elif "headphones" in user_message or "wireless headphones" in user_message:
        return "Wireless Headphones"
    elif "smartphone" in user_message:
        return "Smartphone"
    
    return None


def get_product_details(product_name):
    for product in products.values():
        if product["name"].lower() == product_name.lower():
            return f"{product['name']}: {product['description']} - Price: ${product['price']:.2f}"
    return "Sorry, I couldn't find that product."

def place_order(product_name):
    for product in products.values():
        if product["name"].lower() == product_name.lower():
            return f"Your order for {product['name']} has been placed successfully!"
    return "Sorry, I couldn't place the order for that product."

def chat(request):
    return render(request, 'chatbot/chat.html')
