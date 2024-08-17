from django.urls import path
from .views import ImageDownloadView

urlpatterns = [
    path('download/', ImageDownloadView.as_view(), name='image_download'),
]
# from django.urls import path
# from .views import ImageProcessView

# urlpatterns = [
#     path("process-image/", ImageProcessView.as_view(), name="process_image"),
# ]
