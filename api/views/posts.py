from flask import Blueprint, jsonify, request
from api.middleware import login_required, read_token

from api.models.db import db
from api.models.post import Post

posts = Blueprint('posts', 'posts')

@posts.route('/', methods=["POST"])
@login_required
def create():
  data = request.get_json()
  profile = read_token(request)
  data["profile_id"] = profile["id"]
  post = Post(**data)
  db.session.add(post)
  db.session.commit()
  return jsonify(post.serialize()), 201

@posts.route('/', methods=["GET"])
def index():
  posts = Post.query.all()
  return jsonify([post.serialize() for post in posts]), 200

@posts.route('/<id>', methods=["GET"])
def show(id):
  post = Post.query.filter_by(id=id).first()
  post_data = post.serialize()
  return jsonify(post=post_data), 200

@posts.route('/<id>', methods=["PUT"]) 
@login_required
def update(id):
  data = request.get_json()
  profile = read_token(request)
  post = Post.query.filter_by(id=id).first()

  if post.profile_id != profile["id"]:
    return 'Forbidden', 403

  for key in data:
    setattr(post, key, data[key])

  db.session.commit()
  return jsonify(post.serialize()), 200

@posts.route('/<id>', methods=["DELETE"]) 
@login_required
def delete(id):
  profile = read_token(request)
  post = Post.query.filter_by(id=id).first()

  if post.profile_id != profile["id"]:
    return 'Forbidden', 403

  db.session.delete(post)
  db.session.commit()
  return jsonify(message="Success"), 200


@posts.errorhandler(Exception)          
def basic_error(err):
  return jsonify(err=str(err)), 500
