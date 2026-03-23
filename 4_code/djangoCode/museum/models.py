from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)
 
    def __str__(self):
        return f"{self.user.username} ({self.points} pts)"


class Badge(models.Model):
    code = models.SlugField(unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    points_threshold = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class UserBadge(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    awarded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "badge")

    def __str__(self):
        return f"{self.user.username} -> {self.badge.code}"


class Question(models.Model):
    TEXT = "text"
    MULTIPLE_CHOICE = "mc"

    TYPE_CHOICES = [
        (TEXT, "Text (reflective)"),
        (MULTIPLE_CHOICE, "Multiple choice"),
    ]

    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name="questions")
    prompt = models.TextField()
    qtype = models.CharField(max_length=10, choices=TYPE_CHOICES, default=TEXT)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.quiz.title}: {self.prompt[:40]}"


class AnswerOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
    text = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.text


class QuizAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="quiz_attempts")
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name="attempts")
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.quiz.title} @ {self.submitted_at}"


class Response(models.Model):
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name="responses")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(AnswerOption, null=True, blank=True, on_delete=models.SET_NULL)
    text_answer = models.TextField(blank=True)

    def __str__(self):
        return f"Response({self.attempt_id}, q={self.question_id})"
    
##category model 

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True )
    description = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    display_image = models.ImageField(upload_to='categories/', blank=True, null=True)
    static_image = models.CharField(
        max_length=200, blank=True,
    )

    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name


##exhibit model (extended)
class Exhibit(models.Model):

    #basic info
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='exhibits')
    failure_type = models.CharField(max_length=100, blank=True)
    deployment_context = models.TextField(blank=True)
    intended_use = models.TextField(blank=True)
    artefact1 = models.FileField(upload_to='exhibits/artefacts/', blank=True, null=True)

    #AI system description
    system_type = models.CharField(max_length=100, blank=True)
    inputs_assumptions = models.TextField(blank=True)
    outputs_to_users = models.TextField(blank=True)
    artefact2 = models.FileField(upload_to='exhibits/artefacts/', blank=True, null=True)

    # failure description
    what_went_wrong = models.TextField(blank=True)
    how_detected = models.TextField(blank=True)
    who_affected = models.TextField(blank=True)
    artefact3 = models.FileField(upload_to='exhibits/artefacts/', blank=True, null=True)

    #contributing factors
    data_issues = models.TextField(blank=True)
    design_choices = models.TextField(blank=True)
    org_governance_issues = models.TextField(blank=True)
    artefact4 = models.FileField(upload_to='exhibits/artefacts/', blank=True, null=True)

    #lessons learned
    recommendations = models.TextField(blank=True)
    warnings = models.TextField(blank=True)
    artefact5 = models.FileField(upload_to='exhibits/artefacts/', blank=True, null=True)

    #Short summary of the exhibit
    description = models.TextField()
    is_archived = models.BooleanField(default=False)

    ##to create upload field for the database
    file = models.FileField(upload_to='exhibits/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    ## view tracking — the field stores the count,
    ## the actual incrementing is handled elsewhere (see views.py exhibit_detail)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    ## ── helper queries for search / homepage ──

    @staticmethod
    def top_viewed(n=3):
        """Return the top n most-viewed non-archived exhibits."""
        return Exhibit.objects.filter(is_archived=False).order_by('-view_count')[:n]

    @staticmethod
    def the_rest(n=3):
        """Return every non-archived exhibit EXCEPT the top n most-viewed, ordered by title."""
        top_ids = Exhibit.objects.filter(is_archived=False).order_by('-view_count').values_list('id', flat=True)[:n]
        return Exhibit.objects.filter(is_archived=False).exclude(id__in=top_ids).order_by('title')


class Comment(models.Model):
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} on {self.exhibit.title}: {self.body[:40]}"


class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookmarks')
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE, related_name='bookmarks')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'exhibit')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} bookmarked {self.exhibit.title}"


class UserSubmission(models.Model):
    PENDING = 'pending'
    APPROVED = 'approved'
    DENIED = 'denied'
    STATUS_CHOICES = [
        (PENDING, 'Pending Review'),
        (APPROVED, 'Approved'),
        (DENIED, 'Denied'),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='submissions')
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    what_went_wrong = models.TextField()
    who_affected = models.TextField(blank=True)
    source_url = models.URLField(blank=True)
    artefact = models.FileField(upload_to='submissions/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='reviewed_submissions'
    )
    reviewer_note = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"


class Quiz(models.Model):
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE, related_name='quizzes', null=True, blank=True)  # ADD THIS LINE

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    points_for_completion = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.title

class TimelineEvent(models.Model):
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE, related_name='timeline_events')
    year = models.CharField(max_length=20)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'year']
class ExhibitView(models.Model):
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE, related_name='views')
    session_key = models.CharField(max_length=40)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-viewed_at']

    def __str__(self):
        return f"View on {self.exhibit.title} @ {self.viewed_at}"