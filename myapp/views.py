from django.shortcuts import render
from myapp.models import Song, Watchlater
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.db.models import Case, When

def watchlater(request):
    if not request.user.is_authenticated:
        return redirect('/myapp/login')
        
    if request.method == "POST":
        user = request.user
        video_id = request.POST['video_id']

        watch = Watchlater.objects.filter(user=user)
        
        for i in watch:
            if video_id == i.video_id:
                message = "Your Song is Already Added"
                break
        else:
            watchlater = Watchlater(user=user, video_id=video_id)
            watchlater.save()
            message = "Your Song is Succesfully Added"

        song = Song.objects.filter(song_id=video_id).first()
        return render(request, f"myapp/songpost.html", {'song': song, "message": message})

    wl = Watchlater.objects.filter(user=request.user)
    ids = []
    for i in wl:
        ids.append(i.video_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)

    return render(request, "myapp/watchlater.html", {'song': song})

def songs(request):
    song = Song.objects.all()
    return render(request, 'myapp/songs.html', {'song': song})

def songpost(request, id):
    song = Song.objects.filter(song_id=id).first()
    return render(request, 'myapp/songpost.html', {'song': song})

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)   
            return redirect("/")
        else:
            return render(request, 'myapp/login.html', {'error_message': 'Invalid username or password'})
            
    return render(request, 'myapp/login.html')

def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # 1. Check if passwords match
        if pass1 != pass2:
            return render(request, 'myapp/signup.html', {'error': "Passwords do not match"})

        # 2. Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'myapp/signup.html', {'error': "Username already taken"})

        # 3. Create user
        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()

        # 4. Authenticate before login
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'myapp/signup.html')

def logout_user(request):
    logout(request)
    return redirect("/")

def upload(request):
    if not request.user.is_authenticated:
        return redirect('/myapp/login')
        
    if request.method == "POST":
        name = request.POST['name']
        image = request.FILES.get('image', None)
        
        if 'file' not in request.FILES:
            return render(request, "myapp/upload.html", {'error_message': 'Please select a song file'})
            
        song1 = request.FILES['file']

        song_model = Song(name=name,song=song1)
        if image:
            song_model.image = image
        song_model.save()
            
        return render(request, "myapp/upload.html", {'success_message': 'Song uploaded successfully'})

    return render(request, "myapp/upload.html")