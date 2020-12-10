from django.views.generic.edit import FormView
from .forms import UploadForm
from .models import Attachment
from django.shortcuts import render
from .gem import process_pdf_to_xls

class UploadView(FormView):
    template_name = 'gem/form.html'
    form_class = UploadForm
    success_url = 'process/'

    def form_valid(self, form):
        for each in form.cleaned_data['attachments']:
            Attachment.objects.create(file=each)
        return super(UploadView, self).form_valid(form)


def process(request):
    process_pdf_to_xls(request)
    Attachment.objects.all().delete()
    return render(request, 'gem/process.html')