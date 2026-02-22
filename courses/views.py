from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Course, Question, Answer, TestAttempt, UserAnswer, Lesson


def home(request):
    return render(request, 'home.html')


@login_required
def start_test(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    attempt = TestAttempt.objects.create(
        user=request.user,
        course=course
    )

    return redirect('take_test', attempt_id=attempt.id)


@login_required
def take_test(request, attempt_id):
    attempt = get_object_or_404(TestAttempt, id=attempt_id)
    questions = Question.objects.filter(course=attempt.course)

    if request.method == 'POST':
        score = 0

        for question in questions:
            selected_answer_id = request.POST.get(f'question_{question.id}')

            if not selected_answer_id:
                continue

            try:
                selected_answer = Answer.objects.get(id=selected_answer_id)
            except Answer.DoesNotExist:
                continue

            user_answer = UserAnswer.objects.create(
                attempt=attempt,
                question=question,
                selected_answer=selected_answer
            )

            if user_answer.is_correct:
                score += 1

        attempt.score = score
        attempt.completed_at = timezone.now()
        attempt.passed = score >= questions.count() * 0.7
        attempt.save()

        return redirect('test_result', attempt_id=attempt.id)

    return render(request, 'courses/take_test.html', {
        'attempt': attempt,
        'questions': questions
    })


@login_required
def test_result(request, attempt_id):
    attempt = get_object_or_404(TestAttempt, id=attempt_id)
    user_answers = attempt.user_answers.select_related('question', 'selected_answer')

    return render(request, 'courses/test_result.html', {
        'attempt': attempt,
        'user_answers': user_answers
    })


@login_required
def attempt_list(request):
    attempts = TestAttempt.objects.filter(user=request.user).order_by('-started_at')

    return render(request, 'courses/attempt_list.html', {
        'attempts': attempts
    })


@login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    return render(request, 'courses/lesson_detail.html', {
        'lesson': lesson
    })
