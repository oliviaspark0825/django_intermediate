from django.shortcuts import render, redirect
from .models import Board
# Create your views here.
def index(request):
    boards = Board.objects.order_by('-pk')
    context = {
        'boards': boards,
    }
    return render(request,'board/index.html', context)
    
def new(request):
    return render(request, 'board/new.html')
    
    # 모델하고 작업하는거라 페이지가 필요 없음
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    board = Board(title=title, content=content)
    board.save()
    
    # return redirect(f'/board/{board.pk}/')
    return redirect(f'board:detail', board.pk)

def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board' : board,
    }
    return render(request,'board/detail.html', context)
    
def delete(request,pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    # return redirect('/board/')
    return redirect('board:index')
    
def edit(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'board/edit.html', {'board': board})
    
def update(request,pk):
    board = Board.objects.get(pk=pk)
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    # return redirect(f'/board/{ board.pk }/')
    return redirect(f'board:detail', board.pk)