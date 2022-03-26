from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import Img


# Create your views here.

class Gallery(View):
    def get(self, request):
        img_list = Img.objects.all()
        return render(request, 'gallery.html', {
            'img_list': img_list,
            'title': 'Gallery',
        }, )

    def get_imgs(request):
        nid = request.GET.get('nid')
        img_list = Img.objects.filter(id__gt=nid).values('id', 'src', 'title').order_by('id')
        img_list = list(img_list)
        ret = {
            'status': True,
            'data': img_list
        }
        return JsonResponse(ret)
