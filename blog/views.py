from django.shortcuts import render
from blog.models import Post # Post 모델을 사용하기 위해 import
# Create your views here.

def post_list( request ):

    posts = Post.objects.all() # 모든 Post 객체를 가진 QuerySet

    # 템플릿에 전달한 dict
    context = {
        "posts" : posts,
    }

    # 3번째 인수로 템플릿에 데이터를 전달
    return render(request, "post_list.html", context )