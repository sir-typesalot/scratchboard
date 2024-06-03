from flask import redirect, request, Blueprint, render_template, url_for

tags = Blueprint('tag', __name__, url_prefix='/board')

variables = {
    'title': 'Home',
    'footer_text': 'Scratch Board',
    'cache': 1
}

@tags.route('/<string:hash>/tags', methods=['GET'])
def get_tags(hash):
    return render_template('error.html', data=variables)

@tags.route('/<string:hash>/tags/<int:tag_id>', methods=['GET'])
def get_tag(hash, tag_id):
    return render_template('error.html', data=variables)

@tags.route('/<string:hash>/tags/new', methods=['POST'])
def create_tag(hash, tag_id):
    return render_template('error.html', data=variables)

@tags.route('/<string:hash>/tags/<int:tag_id>/modify', methods=['PUT'])
def modify_tag(hash, tag_id):
    return render_template('error.html', data=variables)

@tags.route('/<string:hash>/tags/<int:tag_id>/modify', methods=['DELETE'])
def delete_tag(hash, tag_id):
    return render_template('error.html', data=variables)
