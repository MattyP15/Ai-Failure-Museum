def is_curator(user) -> bool:
    if not user.is_authenticated:
        return False
    if user.is_staff:
        return True
    return user.groups.filter(name="Curator").exists()
