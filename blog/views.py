from django.shortcuts import render, redirect
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

def post_detail( request, post_id ):
    
    post = Post.objects.get( id = post_id ) # id값이 URL에서 받은 post_id값인 Post객체
    print( post )                           # 가져온 객체를 print 함수로 확인
    
    context = {
        "post" : post,
    }
    return render( request, "post_detail.html", context )

def post_add( request ):
    

    """
    
    단순히 post_add 페이지를 로딩할때는 GET메소드로 요청하고 
    게시물 작성의 입력란을 모두 채우고 작성 버튼을 누르면 POST로 요청한다.
    그래서 views.py파일의 post_add메소드에서도 어떤 요청으로 들어왔는지
    구분해줄 필요가 있다. ( 구분을 안하게 되면 페이지를 로딩할때는 GET메소드로 요청했지만 post_add메소드에서는 오직 POST요청만 처리하므로 에러가 발생한다. )
    
    """
    if request.method == 'POST':    # method가 POST일 때
        # POST 요청일 때는 변수를 할당
        print(request.POST)         # POST 메서드로 전달된 데이터를 출력한다.
        title = request.POST[ "title" ]
        content = request.POST[ "content" ]

        # Post 모델의 create()를 사용해 객체를 생성
        post = Post.objects.create(
            title = title,
            content = content,
        )

        print( title )
        print( content )
        return redirect( f"/posts/{ post.id }/" )
    else:                           # method가 POST가 아닐 때
        print( 'method GET' )
        
    # POST/GET중 어느 요청이든 render 결과를 리턴
    return render( request, "post_add.html" )