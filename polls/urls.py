from django.urls import path
from rest_framework.routers import DefaultRouter

from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, PollViewSet, UserCreate, LoginView

# from rest_framework.documentation import include_docs_urls
# from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

# schema_view = get_swagger_view(title='Polls API')

urlpatterns = [
    path('polls/', PollList.as_view(), name='polls_list'),
    path('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/',
         CreateVote.as_view(), name='create_vote'),
    path('user/', UserCreate.as_view(), name='user_create'),
    path('login/', LoginView.as_view(), name='login'),

    # path(r'docs/', include_docs_urls(title='Polls API')),
    # path(r'swagger-docs/', schema_view),
]

urlpatterns += router.urls
