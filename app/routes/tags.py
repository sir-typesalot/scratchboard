from flask import jsonify, request, Blueprint
from lib.models.TagModel import TagModel

tags = Blueprint('tag', __name__, url_prefix='/board')

variables = {
    'title': 'Home',
    'footer_text': 'Scratch Board',
    'cache': 1
}

@tags.route('/<string:hash>/tags', methods=['GET'])
def get_tags(hash):
    tag_model = TagModel(hash)
    tags = tag_model.get()
    return tags

@tags.route('/<string:hash>/tags/<int:tag_id>', methods=['GET'])
def get_tag(hash, tag_id):
    tag_model = TagModel(hash)
    tag = tag_model.get({'tag_id': tag_id})
    tag = tag[0] if tag else []
    return jsonify(tag)

@tags.route('/<string:hash>/tags/new', methods=['POST'])
def create_tag(hash):
    tag_model = TagModel(hash)
    response = {}
    # Get params
    name = request.json.get('name')
    description = request.json.get('description', '')

    try:
        response['tag_id'] = tag_model.create_new(name, description)
        response['status'] = 200
    except NameError:
        response['tag_id'] = None
        response['status'] = 302

    return jsonify(response)

@tags.route('/<string:hash>/tags/<int:tag_id>/modify', methods=['PUT'])
def modify_tag(hash, tag_id):
    tag_model = TagModel(hash)
    # get tag
    # modify tag
    # return status
    return {}

@tags.route('/<string:hash>/tags/<int:tag_id>/delete', methods=['DELETE'])
def delete_tag(hash, tag_id):
    tag_model = TagModel(hash)
    return {}
