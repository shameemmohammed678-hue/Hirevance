from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import MockTest,TestQuestion,TestAttempt,TestAnswer
# Create your views here.


def Mock_tests(request):
    mock_tests = MockTest.objects.all()


    for test in mock_tests:
        test.question_count = TestQuestion.objects.filter(mock_test = test).count()

    return render(request,'mocktests/mocktests.html',{'mock_tests':mock_tests})


@login_required
def start_test(request,test_id):

    test = MockTest.objects.get(id=test_id)

    attempt = TestAttempt.objects.create(
        user = request.user,
        mock_test = test,
        started_at = timezone.now()
    )
    return redirect('take-test',attempt_id = attempt.id)



@login_required
def take_test(request, attempt_id):

    attempt = get_object_or_404(
        TestAttempt,
        id=attempt_id,
        user=request.user
    )
    if attempt.ended_at:
        return redirect(
            'test-result',
            attempt_id=attempt.id
        )


    questions = TestQuestion.objects.filter(
        mock_test=attempt.mock_test
    ).order_by('order')

    elapsed_seconds = int(
        (timezone.now() - attempt.started_at).total_seconds()
    )

    total_seconds = attempt.mock_test.duration * 60

    remaining_seconds = max(
        total_seconds - elapsed_seconds,
        0
    )

    return render(
        request,
        'mocktests/test.html',
        {
            'attempt': attempt,
            'questions': questions,
            'remaining_seconds': remaining_seconds
        }
    )

@login_required
def submit_test(request, attempt_id):

    attempt = get_object_or_404(
        TestAttempt,
        id=attempt_id,
        user=request.user
    )
    if attempt.ended_at:
        return redirect(
        'test-result',
        attempt_id=attempt.id
    )

    if request.method == 'POST':

        test_questions = TestQuestion.objects.filter(
            mock_test=attempt.mock_test
        )

        score = 0

        for test_question in test_questions:

            question = test_question.question

            selected_option_id = request.POST.get(
                f'question_{question.id}'
            )

            if selected_option_id:

                selected_option = question.questionoption_set.get(
                    id=selected_option_id
                )

                TestAnswer.objects.update_or_create(
                    attempt=attempt,
                    question=question,
                    defaults={
                        'selected_option': selected_option
                    }
                )

                if selected_option.is_correct:
                    score += 1

        total_questions = test_questions.count()

        if total_questions > 0:
            percentage = round(
                (score / total_questions) * 100
            )
        else:
            percentage = 0

        attempt.score = percentage
        attempt.ended_at = timezone.now()
        attempt.save()

        return redirect(
            'test-result',
            attempt_id=attempt.id
        )

@login_required
def test_result(request, attempt_id):

    attempt = get_object_or_404(
        TestAttempt,
        id=attempt_id,
        user=request.user
    )

    answers = TestAnswer.objects.filter(
        attempt=attempt
    )

    correct_answers = answers.filter(
        selected_option__is_correct=True
    ).count()

    answered_questions = answers.count()

    total_questions = TestQuestion.objects.filter(
        mock_test=attempt.mock_test
    ).count()

    wrong_answers = answered_questions - correct_answers

    unanswered = total_questions - answered_questions

    return render(
        request,
        'mocktests/test_result.html',
        {
            'attempt': attempt,
            'total_questions': total_questions,
            'correct_answers': correct_answers,
            'wrong_answers': wrong_answers,
            'unanswered': unanswered,
        }
    )






@login_required
def review_answers(request, attempt_id):

    attempt = get_object_or_404(
        TestAttempt,
        id=attempt_id,
        user=request.user
    )

    test_questions = TestQuestion.objects.filter(
        mock_test=attempt.mock_test
    ).order_by('order')

    review_data = []

    for test_question in test_questions:

        question = test_question.question

        user_answer = TestAnswer.objects.filter(
            attempt=attempt,
            question=question
        ).first()

        correct_answer = question.questionoption_set.filter(
            is_correct=True
        ).first()

        review_data.append({
            'question': question,
            'user_answer': user_answer,
            'correct_answer': correct_answer,
        })

    return render(
        request,
        'mocktests/review.html',
        {
            'attempt': attempt,
            'review_data': review_data
        }
    )