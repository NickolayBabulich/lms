from rest_framework.pagination import PageNumberPagination


class CoursePaginator(PageNumberPagination):
    page_size = 15


class LessonPaginator(PageNumberPagination):
    page_size = 15