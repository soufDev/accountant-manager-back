from django.conf.urls import url

from users.api.views import CandidateList, CandidateDetail, profile_type

urlpatterns = (
    # candidate urls
    url(r'candidates/$', CandidateList.as_view(), name='candidate_list'),
    url(r'candidates/(?P<pk>[0-9]+)/$', CandidateDetail.as_view(), name='candidate_detail'),
    url(r'profile/(?P<pk>[0-9]+)/$', profile_type, name='profile_type'),

    #
)