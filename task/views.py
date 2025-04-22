from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User
from .models import Task
from django.contrib import messages
from .forms import TaskAssignForm , TaskStatusForm, CommentForm





def is_admin(user):
    return user.is_superuser

@login_required
def user_task_list(request):
    tasks = Task.objects.filter(assigned_to=request.user).distinct()
    return render(request, 'task/user_tasks.html', {'tasks': tasks})

@login_required
def task_redirect_view(request):
    if request.user.is_superuser:
        return redirect('task:admin_task_panel')
    else:
        return redirect('task:user_task_list')

@user_passes_test(is_admin)
def admin_task_panel(request):
    users = User.objects.filter(is_superuser=False)  # sadece normal kullanıcılar
    tasks = Task.objects.all().prefetch_related('assigned_to')  # görev listesi

    if request.method == "POST":
        form = TaskAssignForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            form.save_m2m()  # 🔥 kritik satır
            messages.success(request, "Görev başarıyla atandı.")
            return redirect('task:admin_task_panel')
    else:
        form = TaskAssignForm()

    return render(request, 'task/admin_panel.html', {
        'users': users,
        'tasks': tasks,
        'form': form,
    })

@login_required
def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, assigned_to=request.user)
    if request.method == "POST":
        form = TaskStatusForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task:user_task_list')  # görev listesine dön
    else:
        form = TaskStatusForm(instance=task)
    return render(request, 'task/update_status.html', {'form': form, 'task': task})


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, assigned_to=request.user)
    comments = task.comments.all().order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.task = task
            new_comment.user = request.user
            new_comment.save()
            return redirect('task:task_detail', pk=task.pk)
    else:
        form = CommentForm()

    return render(request, 'task/task_detail.html', {
        'task': task,
        'form': form,
        'comments': comments
    })