from rest_framework import pagination

class PageSet(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "limit"
    max_page_size = 100
    page_query_param = "page"