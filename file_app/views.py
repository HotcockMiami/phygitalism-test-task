'''
Описываем своё АПИ, тут ничего сложного, просто прописываем ему откуда брать данные,
в данном случае - мой модуль
'''

from . import converter
from rest_framework.response import Response
from rest_framework.views import APIView

class FilesView(APIView):
    def get(self, request):
        return Response(converter.dir_to_json('./files'))
