from .models import Blog
from .serializers import BlogSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)