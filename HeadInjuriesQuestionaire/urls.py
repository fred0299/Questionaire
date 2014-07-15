from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, ListView, TemplateView
from models import Encounter, CoverSheet
from HeadInjuriesQuestionaire import views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='HeadInjuriesQuestionaire/login.html')),
    url(r'^login/$', 'HeadInjuriesQuestionaire.views.user_login', name='user_login'),
    url(r'^subject/$', TemplateView.as_view(template_name='HeadInjuriesQuestionaire/index.html')),
    url(r'^index/$', views.patientInformation),
    url(r'^(?P<pk>\d+)/coverSheet/$',
        DetailView.as_view(
        model=Encounter,
        template_name='HeadInjuriesQuestionaire/HICoverSheet.html'),
    name='coverSheet'),
    url(r'^(?P<e_id>\d+)/coversheetsubmit/$', 'HeadInjuriesQuestionaire.views.coversheetsubmit', name='coversheetsubmit'),
    url(r'^(?P<pk>\d+)/NonBlastHeadInjury/$',
        DetailView.as_view(
        model=Encounter,
        template_name='HeadInjuriesQuestionaire/NonBlastHeadInjury.html'),
    name='NonBlastHeadInjury'),
    url(r'^(?P<e_id>\d+)/nonBlastHeadInjuryPage1/$', 'HeadInjuriesQuestionaire.views.nonBlastHeadInjuryPage1', name='nonBlastHeadInjuryPage1'),
    url(r'^(?P<pk>\d+)/NonBlastHeadInjury2/$',
        DetailView.as_view(
        model=Encounter,
        template_name='HeadInjuriesQuestionaire/NonBlastHeadInjury2.html'),
    name='NonBlastHeadInjury2'),
    url(r'^(?P<pk>\d+)/NonBlastHeadInjury3/$',
        DetailView.as_view(
        model=Encounter,
        template_name='HeadInjuriesQuestionaire/NonBlastHeadInjury3.html'),
    name='NonBlastHeadInjury3'),
    url(r'^(?P<nbhi_id>\d+)/nonBlastHeadInjuryPage2/$', 'HeadInjuriesQuestionaire.views.nonBlastHeadInjuryPage2', name='nonBlastHeadInjuryPage2'),
    url(r'^(?P<nbhi_id>\d+)/nonBlastHeadInjuryPage3/$', 'HeadInjuriesQuestionaire.views.nonBlastHeadInjuryPage3', name='nonBlastHeadInjuryPage3'),
    url(r'^register/$', 'HeadInjuriesQuestionaire.views.register', name='register'),
    url(r'^restricted/', 'HeadInjuriesQuestionaire.views.restricted', name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    #url(r'^index/confirm/$',
    #    ListView.as_view(
    #    model=CoverSheet,
    #    template_name='HeadInjuriesQuestionaire/confirm.html'),
    #name='confirm'),
)