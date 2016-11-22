__author__ = '0138695'
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

doc = {
    'author': 'juema33',
    'text': '324234: cool. bonsai cool.',
    'timestamp': datetime.now(),
}

res = es.index(index="test-zl-index",doc_type='test',body=doc)
#print(res['created'])

res = es.search(index="test-zl-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

#es.indices.delete(index='test-test')
print("_____________________")
res = es.search(index='test-zl-index', filter_path=['hits.hits._id', 'hits.hits._type'])
print res
print "___________________zl"
res = es.search(index="test-zl-index", doc_type="test")
print res