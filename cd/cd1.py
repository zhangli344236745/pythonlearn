__author__ = '0138695'
from cassandra.cluster import Cluster
import uuid

cluster = Cluster()
session = cluster.connect("demodb")
rows = session.execute('SELECT * FROM BLOG')
for user_row in rows:
    print user_row.id
session.execute("INSERT INTO blog (id,title,content) VALUES (uuid.UUID,'ZHANGLI','LILI')")