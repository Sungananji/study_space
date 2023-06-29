from django.urls import path
from . import views
from classroom.views import Submissions, StudentSubmissions, GradeSubmission
from module.views import NewModule, CourseModules
from page.views import NewPageMdoule, PageDetail, MarkPageAsDone
from quiz.views import (NewQuiz, QuizDetail, NewQuestion, TakeQuiz, SubmitAttempt, AttemptDetail,)
from assignment.views import (NewAssignment, AssignmentDetail, NewSubmission)
from question.views import (NewStudentQuestion, Questions, QuestionDetail, VoteAnswer, MarkAsAnswer)



urlpatterns = [
    # Course -Classroom
    path('new-course/', views.NewCourse, name='new-course'),
    path('my-courses/', views.MyCourse, name='my-courses'),
    path('categories/', views.Categories, name='categories'),
    path('categories/<category_slug>', views.CategoryCourses, name='category-courses'),
    path('<course_id>', views.CourseDetail, name='course'),
    path('<course_id>/enroll', views.Enroll, name='enroll'),
    path('<course_id>/edit', views.EditCourse, name='edit-course'),
    path('<course_id>/delete', views.DeleteCourse, name='delete-course'),

    # Modules
    path('<course_id>/modules/new-module', NewModule, name='new-module'),
    path('<course_id>/modules', CourseModules, name='modules'),

    # Page
    path('<course_id>/modules/<module_id>/pages/new-page', NewPageMdoule, name='new-page'), 
    path('<course_id>/modules/<module_id>/pages/<page_id>', PageDetail, name='page-detail'),
    path('<course_id>/modules/<module_id>/pages/<page_id>/done', MarkPageAsDone, name='mark-page-as-done'),

    # Quiz
    path('<course_id>/modules/<module_id>/quiz/new-quiz', NewQuiz, name='new-quiz'), 
    path('<course_id>/modules/<module_id>/quiz/<quiz_id>/new-question', NewQuestion, name='new-question'),
    path('<course_id>/modules/<module_id>/quiz/<quiz_id>/quiz-detail', QuizDetail, name='quiz-detail'),
    path('<course_id>/modules/<module_id>/quiz/<quiz_id>/take', TakeQuiz, name='take-quiz'),
    path('<course_id>/modules/<module_id>/quiz/<quiz_id>/take/submit', SubmitAttempt, name='submit-quiz'),
    path('<course_id>/modules/<module_id>/quiz/<quiz_id>/<attempt_id>/results', AttemptDetail, name='attempt-detail'),
    
    #Assignment
	path('<course_id>/modules/<module_id>/assignment/new-assignment', NewAssignment, name='new-assignment'),
	path('<course_id>/modules/<module_id>/assignment/<assignment_id>', AssignmentDetail, name='assignment-detail'),
	path('<course_id>/modules/<module_id>/assignment/<assignment_id>/start', NewSubmission, name='start-assignment'),
	#Submissions
	path('<course_id>/submissions', Submissions, name='submissions'),
	path('<course_id>/student-submissions', StudentSubmissions, name='student-submissions'),
	path('<course_id>/submissions/<grade_id>/grade', GradeSubmission, name='grade-submission'),
    #Questions
    path('<course_id>/questions', Questions, name='questions'),
    path('<course_id>/new-question', NewStudentQuestion, name='new-student-question'),
    path('<course_id>/question/<question_id>', QuestionDetail, name='question-detail'),
    path('<course_id>/question/<question_id>/vote', VoteAnswer, name='vote-answer'),
    path('<course_id>/question/<question_id>/<answer_id>/mark-as-answer', MarkAsAnswer, name='mark-as-answer'),
]