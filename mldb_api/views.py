from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import base64

from .serializers import model_serializers, model_serializers_except_base64
from .models import models_repo

# model.h5 base64 로 인코딩
def convert_into_base64(file_path):
    with open(file_path, 'rb') as file:
        base64_string = base64.b64encode(file.read())
    return base64_string

class ModelSave(APIView):
    def post(self, request, format=None):
        #인코딩한 .h5 기계학습 모델 base64 디코딩하여 file_path에 저장
        file_path = '.\media\mldb_api\\' + request.data['model_name'] + '.h5'
        result = open(file_path, 'wb')
        result.write(convert_into_base64(request.data['model_file']))
        request.data['model_base64'] = str(convert_into_base64(request.data['model_file']))
        result.close()

        #request.data check
        # print(request.data)
        print({key: value for key, value in request.data.items() if key != 'model_base64'})
        request.data['model_file'] = file_path

        serializer = model_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # print('saved')
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({key: value for key, value in serializer.data.items() if key != 'model_base64'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        serializer = model_serializers_except_base64(models_repo.objects.all(), many=True)
        return Response(serializer.data)
