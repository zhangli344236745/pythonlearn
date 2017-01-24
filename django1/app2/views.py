__author__ = '0138695'
from django.http import HttpResponse
from app2.models import Teacher
import logging

logger = logging.getLogger(__name__)

def test_db(request):
    obj = Teacher.objects.filter(id__gt = 90,id__lt=99).values("id").order_by("-id")
    print(obj)
    print("________________")
    obj = obj.exclude(id__in=[98,95])
    print(obj)
    return HttpResponse("TEST_DB")

def test_ll(request):
	try:
		a = 1/0
	except:
		logger.warn("wer")
	return HttpResponse("test_ll")
