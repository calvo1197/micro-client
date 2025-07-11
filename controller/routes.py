from flask import Blueprint, request, jsonify
from use_cases import use_cases_client
from entities.model import Client
import logging

client_bp = Blueprint("client_bp", __name__)
request_mapping = "/client"

@client_bp.route(request_mapping, methods=["POST"])
def insert():
    json = request.get_json()
    if not json:
        logging.warning("Empty body insert")
        return {"message": "Empty body"}, 400
    
    try:
        if use_cases_client.insert(Client(**json)):
            logging.info("OK INSERT")
            return {"message": "Inserted"}, 201
    except Exception as ex:
        logging.error("ERROR INSERT: {%s}", ex)
    
    return {"message":"Server error"}, 500

@client_bp.route(request_mapping, methods=["GET"])
def select():
    try:
        data = use_cases_client.select_all()
        if data:
            dictionary = [{
                "id": t.id,
                "name": t.name,
                "address": t.address,
                "email": t.email
                } for t in data]
            logging.info("GET ALL CLIENTS OK")
            return jsonify(dictionary), 200

    except Exception as ex:
        logging.error("ERROR GET ALL CLIENTS: {%s}", ex)

    return {"message": "Server error"}, 500

@client_bp.route(request_mapping, methods=["DELETE"])
def delete():
    id = request.args["id"]
    if not id:
        logging.warning("QUERY PARAMETER ID DOES NOT EXIST")
        return {"message": "Must exists query parameter id"}, 400
    
    try:
        if use_cases_client.delete_by_id(id):
            logging.info("DELETE OK")
            return {"message": "OK"}, 200
        else:
            logging.info("ID {%s} DOES NOT EXIST DELETE", id)
            return {"message": f"Client {id} does not exist"}, 404
    
    except Exception as ex:
        logging.error("ERROR DELETE CLIENT: {%s}", ex)

    return {"message": "Server error"}, 500

@client_bp.route(request_mapping, methods=["PUT"])
def update():
    data = request.get_json()
    if not data:
        logging.warning("Body empty UPDATE")
        return {"message": "EMPTY BODY"}, 400
    
    try:
        if use_cases_client.update(Client(**data)):
            logging.info("UPDATE OK")
            return {"message": "OK"}, 201
        else:
            logging.warning("CLIENT {%s} DOES NOT EXIST", data["id"])
            return {"message": "CLIENT DOES NOT EXIST"}, 404
    
    except Exception as ex:
        logging.error("ERROR UPDATE CLIENT: {%s}", ex)

    return {"message": "Server error"}, 500

