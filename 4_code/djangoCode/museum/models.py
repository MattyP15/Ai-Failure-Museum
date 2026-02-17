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
    slug = models.SlugField(unique=True)   

    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name


##exhibit model (extended)
class Exhibit(models.Model):


    #basic info
    title = models.CharField(max_length=200)
    category= models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) 
    #Domain as in flooding, earthquakes etc
    failure_type = models.CharField(max_length=100, blank=True)
    deployment_context = models.TextField(blank=True)  
    intended_use = models.TextField(blank=True)


    #Ai system desciption 
    system_type = models.CharField(max_length=100, blank=True)  
    inputs_assumptions = models.TextField(blank=True)
    outputs_to_users = models.TextField(blank=True)

    # failure description

    what_went_wrong = models.TextField(blank=True)
    how_detected = models.TextField(blank=True)
    who_affected = models.TextField(blank=True)


    #contributing factors
    data_issues = models.TextField(blank=True)
    design_choices = models.TextField(blank=True)
    org_governance_issues = models.TextField(blank=True)

    #lessons learned
    recommendations = models.TextField(blank=True)
    warnings = models.TextField(blank=True)

    #Short summary of the exhibit
    description = models.TextField()
    is_archived = models.BooleanField(default=False)
    
    ##to create upload field for the database
    file = models.FileField(upload_to='exhibits/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Quiz(models.Model):
    #link exhibit to quiz:
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE, related_name='quizzes', null=True, blank=True)  # ADD THIS LINE

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    points_for_completion = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.title

