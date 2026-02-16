from django.contrib import admin

from .models import (
    UserProfile,
    Badge,
    UserBadge,
    Quiz,
    Question,
    AnswerOption,
    QuizAttempt,
    Response,
)

admin.site.register(UserProfile)
admin.site.register(Badge)
admin.site.register(UserBadge)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(AnswerOption)
admin.site.register(QuizAttempt)
admin.site.register(Response)
