from django.urls import path
from.import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('jobseekerreg/',views.jobseekerreg,name='jobseekerreg'),
    path('view1/',views.view1,name='view1.html'),
    path('detailsview1/<str:pk>',views.detailsview1,name="detailsview1"),
    path('update/<str:pk>',views.update,name="update"),
    path('delete/<str:pk>',views.delete,name="delete"),
    path('employerreg/',views.employerreg,name='employerreg'),
    path('view2/',views.view2,name='view2.html'),
    path('detailsview2/<str:pk>',views.detailsview2,name="detailsview2"),
    path('update2/<str:pk>',views.update2,name="update2"),
    path('delete2/<str:pk>',views.delete2,name="delete2"),
    path('about/',views.about,name='about'),
    path('login/',views.login,name='login.html'),
    path('log/',views.log,name='log'),
    path('loguser/',views.loguser,name='loguser'),
    
    
    
]