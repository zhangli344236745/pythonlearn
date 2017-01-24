from django.http import HttpResponse
from app1.tasks import add
from app1.models import Note,Book
from django.contrib.auth.models import User
# from haystack.query import SearchQuerySet
# from haystack.inputs import Raw
import logging

logger = logging.getLogger(__name__)

def hello(request):
    result = add.delay(3,3)
    print(result.get())
    Note.objects.create(title="zhangli",body="zhanglizhanglizhangli")
    Note.objects.create(title="zhanglili",body="zhanglilizhanglizhanglili")
    return HttpResponse("hello")

# def test_query(request):
#     all_results = SearchQuerySet().all().models(Note)
#     print(all_results.count())
#     hello_results = SearchQuerySet().filter(content='zhanglili')
#     print(hello_results.count())
#     sqs = SearchQuerySet().filter(body=Raw("zhangli"))
#     print(sqs.count())
#     return HttpResponse("test_query")


def test_sf(request):
    #all_r = SearchQuerySet().filter(content="zhangli").models(Book)
    #print(all_r)
    try:
        a = 1/0
    except:
        from raven.contrib.django.raven_compat.models import client
        client.captureException()
    return HttpResponse("TEST_IF")

def test_log(request):
    logger.warn("dsfsdf")
    return HttpResponse("test log")



