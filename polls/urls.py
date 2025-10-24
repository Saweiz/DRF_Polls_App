from django.urls import path

# from .views import polls_list, polls_detail
# from .apiviews import PollList, PollDetail
from .apiviews import ChoiceList, CreateVote, ListVote, UserDetail, UserListCreate, LoginView

# Routers and Viewsets
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewset

# Obtaining token
from rest_framework.authtoken import views

urlpatterns = [
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name='create_vote'),
    path('votes/', ListVote.as_view(), name='list_vote'),
    path('users/', UserListCreate.as_view(), name='user_create'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('login/', LoginView.as_view(), name='login'),
    # custom DRF function
    # path('login/', views.obtain_auth_token, name='login')
]


# Router and Viewset for polls/ aand polls/<int:pk>/
router = DefaultRouter()
router.register("polls", PollViewset, basename="polls")
urlpatterns += router.urls

# Viewset is an Alternate for following function or Class based Views

# Function Based views
# path('polls/', polls_list, name='polls_list'),
# path('polls/<int:pk>/', polls_detail, name='polls_detail'),

## Class based views
# path('polls/', PollList.as_view(), name='polls_list'),
# path('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),
