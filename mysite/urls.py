from django.conf.urls import url, include # include('bookmark.urls') 함수
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('bookmark.urls')),
    # 원래 있던 내용을 모두 bookmark/urls.py 파일로 옮기자.
]