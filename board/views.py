from django.shortcuts import render, redirect
from .models import Board, Comment
# from pprint import pprint
# Create your views here.
def index(request):
    # pprint(request)
    # pprint(type(request))
    # pprint(dir(request))
    # pprint(request.scheme) # http
    # pprint(request.get_host)
    # pprint(request.get_full_path())
    # pprint(request.build_absolute_uri())
    # pprint(request.META) # 에러 페이지 떴을 때 딕셔너리
    # pprint(request.method)
    
    
    boards = Board.objects.order_by('-pk')
    context = {
        'boards': boards,
    }
    return render(request,'board/index.html', context)
    
def new(request):
    if request.method == 'POST':
        #CREATE
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        board = Board(title=title, content=content)
        board.save()
        
        # return redirect(f'/board/{board.pk}/')
        return redirect(f'board:detail', board.pk)
    else:
        return render(request, 'board/new.html')
    

def detail(request, board_pk):
    board = Board.objects.get(pk=board_pk)
    comments = board.comment_set.all()
    
    context = {
        'board' : board,
        'comments' : comments,
    }
    return render(request,'board/detail.html', context)
    
def delete(request,board_pk):
    board = Board.objects.get(pk=board_pk)
    if request.method == 'POST':
        
        board.delete()
    # return redirect('/board/')
        return redirect('board:index')
    else:
        return redirect('board:detail', board.pk)
    # 포스트 방식으로만 삭제할 수 있게
    
    
def edit(request, board_pk):
    if request.method == 'POST':
        # UPDATE
        board = Board.objects.get(pk=board_pk)
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        # return redirect(f'/board/{ board.pk }/')
        return redirect(f'board:detail', board.pk)
    else:#EDIT
        board = Board.objects.get(pk=board_pk)
        return render(request, 'board/edit.html', {'board': board})



# 댓글 함수들 


def comments_create(request,board_pk):
    # 댓글을 달 게시물 가지고오기
    board = Board.objects.get(pk = board_pk)
    # form 에서 넘어온 comment data
    content = request.POST.get('content')
    
    # 댓글 생성 및 저장
    # board에 board 전체 객체를 집어넣으면, 지가 알아서 빼냄
    # orm은 객체를 넣어야 함
    comment = Comment(board=board, content = content)
    comment.save()
    return redirect('board:detail', board.pk)
    
def comments_delete(request, board_pk, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    if request.method == 'POST':
        comment.delete()
        return redirect(f'board:detail', board_pk)
    else:
        return redirect(f'board:detail', board_pk)