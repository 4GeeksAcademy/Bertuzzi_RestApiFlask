import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)


jackson_family = FamilyStructure("Jackson")


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def handle_hello():
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }


    return jsonify(response_body), 200


@app.route('/members', methods=['POST'])
def new_member():
    member = request.json
    if not 'first_name' in member or not 'age' in member or not 'lucky_numbers' in member:
            return 'Mandatory data missing!', 400
    else:
        new_member = jackson_family.add_member(member)
        response_body = {
            "message":"new member added to family Jackson!",
            "results": new_member
        }
        return response_body,200


@app.route('/member/<int:member_id>', methods = ['GET'])
def fetch_member(member_id):
    if any(obj['id'] == member_id for obj in jackson_family._members):
        member = jackson_family.get_member(member_id)
        response_body = {
            "message": "member fetched",
            "results": member
        }
        return response_body, 200
    else:
        return 'Member not found', 404
    

@app.route('/member/<int:member_id>', methods = ['DELETE'])
def delete_member(member_id):
    if any(obj['id'] == member_id for obj in jackson_family._members):
        jackson_family.delete_member(member_id)
        response_body = {
            "message":"Member deleted",
            "updated family":jackson_family._members
        }
        return response_body,200
    else:
        return 'Member not found', 404


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
