from django.shortcuts import render, redirect
from .models import Board
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
    

def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board' : board,
    }
    return render(request,'board/detail.html', context)
    
def delete(request,pk):
    board = Board.objects.get(pk=pk)
    if request.method == 'POST':
        
        board.delete()
    # return redirect('/board/')
        return redirect('board:index')
    else:
        return redirect('board:detail', board.pk)
    # 포스트 방식으로만 삭제할 수 있게
    
    
    
def edit(request, pk):
    if request.method == 'POST':
        # UPDATE
        board = Board.objects.get(pk=pk)
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        # return redirect(f'/board/{ board.pk }/')
        return redirect(f'board:detail', board.pk)
    else:#EDIT
        board = Board.objects.get(pk=pk)
        return render(request, 'board/edit.html', {'board': board})
        