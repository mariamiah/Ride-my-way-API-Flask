from flask import current_app as app
from flask import request, make_response, jsonify
from ..models.users import User, db
import bcrypt

@app.route("/api/v1/auth/signup", methods=["POST"])
def register():
    """Create a new user via query string parameters."""
    data = request.get_json()
    username = data['username']
    name = data['name']
    email = data['email']
    password = data['password'].encode('utf-8')
    phone_number = data['phone_number']
    role = data['role']
    if username and email:
        existing_user = User.query.filter(
            User.username == username or User.email == email
        ).first()
        if existing_user:
            return jsonify({"message": (f"{username}({email}) already created!")}), 409
        new_user = User(
            username=username,
            email=email,
            name=name,
            password=bcrypt.hashpw(password, bcrypt.gensalt(14)),
            phone_number=phone_number,
            role=role,
        )
        db.session.add(new_user)
        db.session.commit()
    return jsonify({"message": (f"{username}({email}) successfully created!")}), 201

