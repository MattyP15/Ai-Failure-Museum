from museum.models import UserProfile


def user_points(request):
    points = 0
    if request.user.is_authenticated:
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        points = profile.points
    return {'user_points': points}
