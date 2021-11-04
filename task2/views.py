from task2.forms import ReviewForm
from django.views.generic.edit import FormView
from django.http import HttpResponse


class ReviewEmailView(FormView):
    template_name = 'review.html'
    form_class = ReviewForm

    def form_valid(seld, form):
        form.send_email()
        msg = "Thanks for the review!"
        return HttpResponse(msg)




