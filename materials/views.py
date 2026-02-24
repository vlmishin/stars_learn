from django.shortcuts import get_object_or_404, redirect, render
from .models import Section, Topic, Lesson


def topic_redirect(request, section_slug, topic_slug):
    section = get_object_or_404(Section, slug=section_slug)
    topic = get_object_or_404(Topic, section=section, slug=topic_slug)

    first_lesson = topic.lessons.first()

    if first_lesson:
        return redirect(first_lesson.get_absolute_url())

    return redirect('home')  # если вдруг уроков нет


def topic_detail(request, section_slug, topic_slug):
    section = get_object_or_404(Section, slug=section_slug)
    topic = get_object_or_404(Topic, slug=topic_slug, section=section)

    lessons = topic.lessons.all().order_by('id')  # или по какому порядку нужно

    # Sidebar logic как раньше
    topics_count = section.topics.count()
    lessons_count = Lesson.objects.filter(topic__section=section).count()
    if topics_count == 1 and lessons_count == 1:
        sidebar_sections = Section.objects.exclude(id=section.id)
    else:
        sidebar_sections = Section.objects.filter(id=section.id)

    return render(request, 'materials/topic.html', {
        'section': section,
        'topic': topic,
        'lessons': lessons,
        'sidebar_sections': sidebar_sections,
    })
