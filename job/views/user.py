from rest_framework.decorators import action
from rest_framework.response import Response

from job.models import Role
from job.models.user import User
from job.serializers.user import UserSerializer, LoginSerializer, LogOutSerializer
from job.views import BaseModelViewSet


class UserView(BaseModelViewSet):
    queryset = User.objects.order_by('-id')
    serializer_class = UserSerializer

    # 用户登录
    @action(methods=['post'], detail=False, url_path='login', url_name='login',
            authentication_classes=[], permission_classes=[], serializer_class=LoginSerializer)
    def login(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        response_date = serializer.create(serializer.data)
        return Response(response_date)

    @action(methods=['post'], detail=False, url_path='logout', url_name='logout',
            serializer_class=LogOutSerializer)
    def logout(self, request):
        athorization = request.META.get('HTTP_AUTHORIZATION') or request.GET.get('Authorization')
        LogOutSerializer.logout(athorization)
        return Response()
