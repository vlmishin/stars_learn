from .models import Section

def sections_processor(request):
    return {
        'sections': Section.objects.prefetch_related('topics')
    }


def sections_context(request):
    return {
        'sections': Section.objects.all().order_by('id')
    }