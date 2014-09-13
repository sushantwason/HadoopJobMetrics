import MetadataConnector
import Utilities

CONFIG_FILE='../conf/queries.conf'

class ReportGenerator(object):
    def __init__(self, dsn='job_metadata_dsn'):
	self.generator=Report(dsn)
	self.queryDict={}

    def readConfig(self):
	f=open(CONFIG_FILE,'r')
        next(f)
	for line in f:
		try:
                        desc,query=line.strip().split(':')
                except Exception:
                        print " Incorrect query conf format detected " 
                        exit(1)
                if not desc or not query:
                        print " Either the description or the query string has been detected as empty, please enter a valid query or description"
                        exit(1)
                desc=Utilities.formatString(desc)
		query=Utilities.formatString(query)
		self.queryDict[desc]=query
        f.close()

     
    def Generate(self):
        for key in self.queryDict:
                desc=key
                query=self.queryDict[desc]
                metric=self.generator.executeQuery(query)
                Utilities.outputGenerator(desc,metric)



    def generateReport(self):
	self.readConfig()
	self.Generate()

    


class Report(object):
    def __init__(self, dsn='job_metadata_dsn'):
	self.queryGen=MetadataConnector.QueryGenerator(dsn)
	

    def executeQuery(self,query):
	metric=self.queryGen.Execute(query)
	return metric

