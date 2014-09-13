# mysql -h pit-prod-etlhive1.snc1 -ucerebro_user -pcerebro_pass cerebro_stats
import MySQLdb


class QueryGenerator(object):
    def __init__(self, dsn='job_metadata_dsn'):
	self.queryGen=MetadataConnect(dsn)
    
    def Execute(self,query):
	return self.queryGen.invoke(query) 



    


class MetadataConnect(object):
    def __init__(self, dsn='ob_metadata_dsn'):
        self.dsn=dsn
	self.host="hostname"
        self.user="user"
        self.passwd="pass"
        self.database="stats"
        self.port=3306
        self.db=MySQLdb.connect(host=self.host, user=self.user,passwd=self.passwd, db=self.database, port=self.port)
        self.db.autocommit(True)



    def invoke(self,query):
	metric=self.queryGenerator(query)
        return metric


    def queryGenerator(self,query):
	cur=self.db.cursor()
        cur.execute('%s' %query)
        queryOutput=cur.fetchall()
        cur.close()
	return queryOutput




