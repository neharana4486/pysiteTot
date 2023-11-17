from flask_app import app
from flask import jsonify, request

# Add initial User
current_id = 0
users = {str(current_id): {"name": "Jonass"}}


@app.route("/api/users", methods=["GET", "POST"])
def handle_users():
    global current_id
    if request.method == "GET":
        return jsonify({"users": users})

    elif request.method == "POST":
        # Recieved new request to add a user
        try:
            data = request.get_json()
            print("printing the data recieved from frontend", data)
            current_id += 1
            users[str(current_id)] = data

            return jsonify({"message": "Users updated successfully"})
        except Exception as e:
            print("Error occured: ", e)
            return jsonify({"message": "could not update users"}), 500


@app.route("/api/users/<user_id>", methods=["GET", "PUT", "DELETE"])
def handle_user(user_id):
    """
    This function takes an ID as dynamic URL parameter, for example 0
    Note:
    - GET method is only available for debugging purposes, to test for a specific user
    open the browser with for example http://localhost:5000/api/users/0 to see the data

    - The assignment is to implement the PUT and DELETE methods for the specific ID, see assignment for specific instructions
    """
    if user_id in users:
        if request.method == "GET":
            print("this is GET request")
            return jsonify(users[user_id])
        elif request.method == "PUT":
            data = request.get_json()
            print("printing the data recieved from frontend", data)
            users[user_id] = data
            print("this is PUT to update", str(users[user_id]))
            return jsonify(users[user_id])
        elif request.method == "DELETE":
            print("printing the remaining data (after delete)")
            del users[user_id]
            return jsonify({"message": "Users has been deleted successfully"})

    else:
        return jsonify({"message": "User not found"}), 404
