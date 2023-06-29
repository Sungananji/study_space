from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import Course, Category, Grade
from .forms import NewCourseForm

# Create your views here.

@login_required
def index(request):
    user = request.user
    courses = Course.objects.filter(enrolled=user)
    
    context = {
        'courses': courses
    }
    return render(request, 'index.html', context)


def Categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'classroom/categories.html', context)


def CategoryCourses(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    courses = Course.objects.filter(category=category)
    context = {
        'courses': courses,
        'category': category
    }
    return render(request, 'classroom/category-courses.html', context)

def CourseDetail(request, course_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)
    teacher_mode = False
    if user == course.user:
        teacher_mode = True
    context = {
        'course':course,
        'teacher_mode': teacher_mode,
    }
    return render(request, 'classroom/course.html', context)

@login_required(login_url='login')
def NewCourse(request):
    user = request.user
    if request.method == 'POST':
        form = NewCourseForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            syllabus = form.cleaned_data.get('syllabus')
            category = form.cleaned_data.get('category')
            Course.objects.create(
                user=user,
                picture=picture,
                title=title,
                description=description,
                syllabus=syllabus,
                category=category,
            )
            return redirect('my-courses')
    else:
        form = NewCourseForm()
    context = {
        'form': form
    }
    return render(request, 'classroom/new-course.html', context)


@login_required(login_url='login')
def Enroll(request, course_id):
    user = request.user
    course = get_object_or_404(Course, id=course_id)
    course.enrolled.add(user)
    return redirect('index')


@login_required(login_url='login')
def DeleteCourse(request, course_id):
    user = request.user
    course = get_object_or_404(Course, course_id)
    if user != course.user:
        return HttpResponseForbidden('You are Not Allowed Here!')
    else:
        course.delete()
    return redirect('my-courses')


@login_required(login_url='login')
def EditCourse(request, course_id):
    course = Course.objects.get(id=course_id)
    user = request.user
    if user != course.user:
        return HttpResponseForbidden('YOU ARE NOT ALLOWED HERE!!')
    else:
        if request.method == 'POST':
            form = NewCourseForm(request.POST, request.FILES, instance=course)
            if form.is_valid():
                picture = request.POST.get('picture')
                title = request.POST.get('title')
                description = request.POST.get('description')
                syllabus = request.POST.get('syllabus')
                category = request.POST.get('category')
                form.save()
                return redirect('my-courses')
        else:
            form = NewCourseForm(request.POST, request.FILES, instance=course)

    context = {
        'form': form,
        'course': course
    }
    return render(request, 'classroom/edit-course.html', context)


def MyCourse(request):
    user = request.user
    courses = Course.objects.filter(user=user)
    context = {
        'courses':courses
    }
    return render(request, 'classroom/my-courses.html', context)

def Submissions(request, course_id):
	user = request.user
	course = get_object_or_404(Course, id=course_id)
	grades = Grade.objects.filter(course=course, submission__user=user)
	context = {
		'grades': grades,
		'course': course
	}
	return render(request, 'classroom/submissions.html', context)

def StudentSubmissions(request, course_id):
	user = request.user
	course = get_object_or_404(Course, id=course_id)
	if user != course.user:
		return HttpResponseForbidden()
	else:
		grades = Grade.objects.filter(course=course)
		context = {
			'course': course,
			'grades': grades,
		}
	return render(request,'classroom/student-grades.html', context)

def GradeSubmission(request, course_id, grade_id):
	user = request.user
	course = get_object_or_404(Course, id=course_id)
	grade = get_object_or_404(Grade, id=grade_id)

	if user != course.user:
		return HttpResponseForbidden()
	else:
		if request.method == 'POST':
			points = request.POST.get('points')
			grade.points = points
			grade.status = 'graded'
			grade.graded_by = user
			grade.save()
			return redirect('student-submissions', course_id=course_id)
	context = {
		'course': course,
		'grade': grade,
          
	}

	return render(request, 'classroom/grade-submission.html', context)