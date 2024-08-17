import os
import requests
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from PIL import Image
from io import BytesIO
import json
from pathlib import Path
from urllib.parse import urlparse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name="dispatch")
class ImageDownloadView(View):
    def post(self, request):
        image_url = json.loads(request.body).get("image_url")
        if not image_url:
            return JsonResponse({"error": "No image URL provided"}, status=400)

        try:
            # Download image
            response = requests.get(image_url)
            if response.status_code != 200:
                return JsonResponse({"error": "Failed to download image"}, status=400)

            # Save image temporarily
            parsed_url = urlparse(image_url)
            image_name = os.path.basename(parsed_url.path)
            # Define the path to save the image
            media_path = Path(settings.MEDIA_ROOT) / image_name

            # Write the image content to the media folder
            with open(media_path, 'wb') as file:
                file.write(response.content)

            # Process image with model (bạn cần thêm phần này tùy vào mô hình của bạn)
            # processed_image_path = self.process_image(image_path)

            # return JsonResponse({'processed_image': processed_image_path}, status=200)
            # Return a success response with the saved image path
            return JsonResponse({'message': 'Image downloaded successfully', 'path': str(Path(settings.MEDIA_URL) / image_name)}, status=200)
        

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


#     # def process_image(self, image_path):
#     #     # Dummy function: Replace with actual model processing
#     #     # Giả sử xử lý ảnh và lưu kết quả vào processed_image_path
#     #     processed_image_path = image_path.replace('.jpg', '_processed.jpg')

#     #     # Dummy example: Just copy the image as processed image (for demonstration)
#     #     image = Image.open(image_path)
#     #     image.save(processed_image_path)

#     #     return processed_image_path
