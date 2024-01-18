from django.shortcuts import render, redirect
from posts.models import Post, Comment, PostImage, HashTag
# from posts.forms import CommentForm, PostForm
from posts.forms import CommentForm, NoticeWriteForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse


# Create your views here.


def feeds(request):
    # if not request.user.is_authenticated:
    #     return redirect("/users/login/")
    print(request.user)
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        "posts": posts,
        "comment_form": comment_form,
    }
    return render(request, "posts/feeds.html", context)


@require_POST
def comment_add(request):
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()

        # url로 next 값을 전달 받으면, 댓글 작성 완료 후 전달받은 값으로 이동
        if request.GET.get("next"):
            url_next = request.GET.get("next")
        # next 값을 전달받지 않았다면, 피드 페이지의 글 위치로 이동
        else:
            url_next = reverse("posts:feeds") + f"#post-{comment.post.id}"

        return HttpResponseRedirect(url_next)


@require_POST
def comment_delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.user == request.user:
        comment.delete()
        url = reverse("posts:feeds") + f"#post-{comment.post.id}"
        return HttpResponseRedirect(url)
    else:
        return HttpResponseForbidden("이 댓글을 삭제할 권한이 없습니다.")


def post_add(request):
    if not request.user.is_authenticated:
        return redirect("/users/login/")
    
    if request.method == "POST":
        # content는 POSTFORM처리
        # form = PostForm(request.POST)
        form = NoticeWriteForm(request.POST)

        if form.is_valid():
            # user값은 request에서 가져와 자동 할당
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            # post 생성 후 전송받은 이미지들을 순회하며 postimage 객체 생성
            for image_file in request.FILES.getlist("images"):
                # model으 imagefield에 바로 할당
                PostImage.objects.create(
                    post=post,
                    photo=image_file,
                )

            # tags에 전달된 문자열을 분리하여 해쉬태그 생성
            tag_string = request.POST.get("tags")
            if tag_string:
                tag_names = [tag_name.strip() for tag_name in tag_string.split(",")]
                for tag_name in tag_names:
                    tag, _ = HashTag.objects.get_or_create(name=tag_name)
                    post.tags.add(tag)

            # 생성 완료 후 피드페이지로 이동하여 생성된 post의 위치로 돌아옴
            url = reverse("posts:feeds") + f"#post-{post.id}"
            return HttpResponseRedirect(url)

    # get에선 빈 form 출력
    else:
        form = NoticeWriteForm()

    context = {"form": form}
    return render(request, "posts/post_add.html", context)

def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.user == request.user:
        post.delete()
        url = reverse("posts:feeds")
        return HttpResponseRedirect(url)
    else:
        return HttpResponseForbidden("이 댓글을 삭제할 권한이 없습니다.")


def tags(request, tag_name):
    try:
        tag = HashTag.objects.get(name=tag_name)
    except HashTag.DoesNotExist:
        posts = Post.objects.none()
    else:
        posts = Post.objects.filter(tags=tag)

    context = {
        "tag_name": tag_name,
        "posts": posts,
    }
    return render(request, 'posts/tags.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comment_form = CommentForm()
    context = {
        "post": post,
        "comment_form": comment_form,
    }
    return render(request, "posts/post_detail.html", context)

# url에서 좋아요 처리할 Post의 id를 전달 받는다


def post_like(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user

    # 사용자가 "좋아요를 누른 post 목록"에 "좋아요 버튼을 누른 Post"가 존재한다면
    if user.like_posts.filter(id=post.id).exists():
        # 좋아요 목록에서 삭제
        user.like_posts.remove(post)

    # 존재하지 않는 다면, 좋아요 목록에 추가
    else:
        user.like_posts.add(post)

    # next로 값이 전달되었다면 해당 위치로, 전달되지 않았다면 피드 페이지에서 해당 Post 위치로 이동.
    url_next = request.GET.get("next") or reverse("posts:feeds") + f"#post-{post.id}"
    return HttpResponseRedirect(url_next)
