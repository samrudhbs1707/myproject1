from django.shortcuts import render, redirect, get_object_or_404
from .models import LiveSession
import uuid

def start_session(request):
    if request.method == "POST":
        unique_id = str(uuid.uuid4())
        session_type = "live"
        userurl = f"http://localhost:8000/session/{unique_id}/"

        # Save to database
        LiveSession.objects.create(
            type=session_type,
            unique_id=unique_id,
            userurl=userurl
        )
        return redirect('session_view', unique_id=unique_id)

    return render(request, 'start.html')


def session_view(request, unique_id):
    session = get_object_or_404(LiveSession, unique_id=unique_id)
    return render(request, 'video.html', {'session': session})
