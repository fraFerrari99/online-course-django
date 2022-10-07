from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here
class ChoiceInline(admin.StackedInline):
    #a question can have a maximum of 4 answers
    #so here we put that choice has an extra field equal to 4
    model = Choice
    extra = 4

class QuestionInline(admin.StackedInline):
    extra = 10 #ten questions for each courses
    model = Question
    
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('text','course')
    search_fields = ['text']

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# <HINT> Register Question and Choice models here
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
