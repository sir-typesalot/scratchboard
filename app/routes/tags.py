from flask import request, Blueprint
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
    return tag[0] if tag else []

@tags.route('/<string:hash>/tags/new', methods=['POST'])
def create_tag(hash):
    tag_model = TagModel(hash)
    # Get params
    name = request.json.get('name')
    description = request.json.get('description')

    tags = tag_model.create_new(name, description)
    return tags

@tags.route('/<string:hash>/tags/<int:tag_id>/modify', methods=['PUT'])
def modify_tag(hash, tag_id):
    tag_model = TagModel(hash)
    # get tag
    # modify tag
    # return status
    return {}

@tags.route('/<string:hash>/tags/<int:tag_id>/delete', methods=['DELETE'])
def delete_tag(hash, tag_id):
    return {}
