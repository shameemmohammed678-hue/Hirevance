from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Question,Category,Bookmark
# Create your views here.

@login_required
def questions_list(request):

    questions = Question.objects.all()
    categories = Category.objects.all()

    selected_category = request.GET.get('category')
    selected_difficulty = request.GET.get('difficulty')

    if selected_category:
        questions = questions.filter(
            category_id=selected_category
        )

    if selected_difficulty:
        questions = questions.filter(
            difficulty = selected_difficulty
        )

    context = {
        'questions': questions,
        'categories': categories,
        'selected_category': selected_category,
        'selected_difficulty':selected_difficulty
    }

    return render(
        request,
        'questions/question_list.html',
        context
    )



@login_required
def question_detail(request, question_id):

    question = Question.objects.get(id=question_id)
    options = question.questionoption_set.all()

    bookmarked = Bookmark.objects.filter(
        user=request.user,
        question=question
    ).exists()

    context = {
        'question': question,
        'options': options,
        'bookmarked': bookmarked
    }

    return render(
        request,
        'questions/question_detail.html',
        context
    )




@login_required
def bookmark_questions(request, question_id):

    question = Question.objects.get(id=question_id)

    bookmark = Bookmark.objects.filter(
        user=request.user,
        question=question
    ).first()

    if bookmark:
        bookmark.delete()
    else:
        Bookmark.objects.create(
            user=request.user,
            question=question
        )

    return redirect(
        'question-detail',
        question_id=question.id
    )





@login_required
def bookmarks(request):

    bookmarks = Bookmark.objects.filter(
        user=request.user
    ).select_related(
        'question',
        'question__category'
    ).order_by('-created_at')

    return render(
        request,
        'questions/bookmarks.html',
        {'bookmarks': bookmarks}
    )