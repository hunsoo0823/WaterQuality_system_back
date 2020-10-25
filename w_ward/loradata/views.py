import json

from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render

from .models import loradata


def index(request):
    datas = loradata.objects.all()
    context = {
        "datas": datas
    }
    return render(request, 'index.html', context)

class IndexView(View):

    def get(selfs, request) :
        lora = loradata.objects.all().order_by('-id')
        data = json.loads(serialize('json',lora))
        return JsonResponse({'data':data})

    def post(self, request):
        if request.META['CONTENT_TYPE'] == 'application/json':
            request = json.loads(request.body)
            lora = loradata(phValue = request['phValue'],
                            doValue = request['doValue'],
                            orpValue = request['orpValue'],
                            tdsValue = request['tdsValue'],
                            turValue = request['turValue'])
        else:
            lora = loradata(phValue = request.POST['phValue'],
                            doValue = request.POST['doValue'],
                            orpValue = request.POST['orpValue'],
                            tdsValue = request.POST['tdsValue'],
                            turValue = request.POST['turValue'])
        lora.save()
        return HttpResponse(status=200)

    def put(self, requset):
        requset = json.loads(requset.body)
        id = requset['id']
