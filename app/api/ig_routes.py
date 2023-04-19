from . import api
from ..models import Post
from flask import abort 

@api.get('/posts')
def getPostsAPI():
    posts = Post.query.all()
    return {
        'status':' ok',
        'results': len(posts),
        'posts': [p.to_dict() for p in posts]
    }

@api.get('/posts/<int:post_id>')
def getPostAPI(post_id):
    post = Post.query.get(post_id)
    if post:
        return {
            'status':' ok',
            'results': 1,
            'post': post.to_dict()
        }
    else:
        return {
            'status': 'not ok',
            'message': 'The post you are looking for does not exist'
        }, 404