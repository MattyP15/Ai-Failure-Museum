from django.db import transaction

from .models import Badge, UserBadge, UserProfile


@transaction.atomic
def award_points(user, points: int):
    profile, _ = UserProfile.objects.get_or_create(user=user)

    profile.points += max(0, int(points))
    profile.save()

    newly_awarded = []
    eligible = Badge.objects.filter(points_threshold__lte=profile.points).order_by("points_threshold")

    for badge in eligible:
        obj, created = UserBadge.objects.get_or_create(user=user, badge=badge)
        if created:
            newly_awarded.append(badge)

    return profile.points, newly_awarded
