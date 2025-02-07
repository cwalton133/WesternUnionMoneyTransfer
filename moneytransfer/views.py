from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Sender, Receiver, Transaction, Agent
from .forms import SenderForm, ReceiverForm, TransactionForm, UserRegisterForm

# Create your views here.

def home(request):
    """
    Home page view.
    """
    return render(request, 'home.html')


def register(request):
    """
    User registration view.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    """
    User login view.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')


def user_logout(request):
    """
    User logout view.
    """
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


def dashboard(request):
    """
    User dashboard view.
    """
    sender = get_object_or_404(Sender, user=request.user)
    transactions = Transaction.objects.filter(sender=sender)
    return render(request, 'dashboard.html', {'transactions': transactions})


def send_money(request):
    """
    Send money view.
    """
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            sender = get_object_or_404(Sender, user=request.user)
            transaction.sender = sender
            transaction.mtcn = generate_mtcn()  # Assume you have a function to generate MTCN
            transaction.save()
            messages.success(request, 'Money sent successfully!')
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'send_money.html', {'form': form})


def receive_money(request):
    """
    Receive money view.
    """
    if request.method == 'POST':
        receiver_form = ReceiverForm(request.POST)
        if receiver_form.is_valid():
            receiver = receiver_form.save()
            messages.success(request, 'Receiver registered successfully!')
            return redirect('dashboard')
    else:
        receiver_form = ReceiverForm()
    return render(request, 'receive_money.html', {'form': receiver_form})


def track_transaction(request):
    """
    Track transaction view using MTCN.
    """
    if request.method == 'POST':
        mtcn = request.POST.get('mtcn')
        transaction = get_object_or_404(Transaction, mtcn=mtcn)
        return render(request, 'track_transaction.html', {'transaction': transaction})
    return render(request, 'track_transaction.html')


def generate_mtcn():
    """
    Function to generate unique MTCN.
    """
    import random
    import string
    return ''.join(random.choices(string.digits, k=15))


