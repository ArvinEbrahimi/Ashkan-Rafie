from django.shortcuts import render, get_object_or_404
from .models import faq,SingleTrack
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
# Create your views here.
def music_page(request):
    
    faqs = faq.objects.all()
    tracks = SingleTrack.published.all()
    recent_tracks = SingleTrack.objects.all().order_by("-published_at")[:4]
    return render(request, "music/music.html",{'faqs':faqs,'tracks':tracks, 'recent_tracks':recent_tracks,})




def singletrack_page(request, page_num):
    tracks = SingleTrack.published.all()
    paginator = Paginator(tracks, 6)

    try:
        this_page_tracks = paginator.page(page_num)
    except PageNotAnInteger:
        this_page_tracks = paginator.page(1)
    except EmptyPage:
        this_page_tracks = paginator.page(paginator.num_pages)
    except InvalidPage:
        this_page_tracks = paginator.page(1)

    recent_tracks = SingleTrack.objects.all().order_by("-published_at")[:3]

    context = {
        "tracks": this_page_tracks,
        "recent_tracks": recent_tracks,
        "paginator": paginator,
    }

    return render(request, "music/SingleTracks.html", context)


def singletrack_detail(request, slug):
    track = get_object_or_404(SingleTrack, slug=slug, status=True)
    return render(request, "music/SingleTracks_detail.html", {"track": track})