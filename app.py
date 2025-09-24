# Import necessary modules from the Flask framework
from flask import Flask, request, jsonify

# Create a Flask web application instance
app = Flask(__name__)

# --- Mock Database ---
# This is a hardcoded list of receipt objects that serves as a
# simulated database for demonstration purposes. In a real-world
# application, this would be a connection to a database like PostgreSQL or MongoDB.
receipts_database = [
    {"receiptId": "ABC-123", "storeName": "Awesome Retail", "totalAmount": 55.75},
    {"receiptId": "DEF-456", "storeName": "Tech Gadgets", "totalAmount": 120.50},
    {"receiptId": "GHI-789", "storeName": "Gourmet Groceries", "totalAmount": 22.99},
    {"receiptId": "JKL-012", "storeName": "Urban Outfitters", "totalAmount": 88.00},
]

# --- API Endpoints ---

@app.route("/verify", methods=["POST"])
def verify_receipt():
    """
    Handles a POST request to verify a receipt against the mock database.
    The function expects a JSON payload containing the receipt details.
    """
    # Use a try-except block to handle potential errors with JSON parsing
    try:
        # Get the JSON data sent in the request body
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "Invalid JSON payload."}), 400

        # Extract the receipt details from the JSON data
        receipt_id = data.get("receiptId")
        store_name = data.get("storeName")
        total_amount = data.get("totalAmount")

        # Basic validation to ensure required fields are present
        if not all([receipt_id, store_name, total_amount]):
            return jsonify({"status": "error", "message": "Missing receipt details."}), 400

        # --- Search Logic ---
        # Find a matching receipt in the mock database
        matching_receipt = None
        for receipt in receipts_database:
            # Normalize store name for case-insensitive comparison
            if (
                receipt["receiptId"] == receipt_id
                and receipt["storeName"].lower()a == store_name.lower()
                and receipt["totalAmount"] == total_amount
            ):
                matching_receipt = receipt
                break  # Exit the loop once a match is found

        # --- Response Generation ---
        if matching_receipt:
            # If a match is found, return a success message with the data
            return jsonify({
                "status": "success",
                "message": "Receipt verified successfully.",
                "data": matching_receipt
            })
        else:
            # If no match is found, return a failure message
            return jsonify({
                "status": "failure",
                "message": "Receipt verification failed. No matching receipt found."
            })

    except Exception as e:
        # Catch any unexpected errors and return a generic server error message
        print(f"An error occurred: {e}")
        return jsonify({"status": "error", "message": "An internal server error occurred."}), 500

# This block ensures the application runs only when the script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
