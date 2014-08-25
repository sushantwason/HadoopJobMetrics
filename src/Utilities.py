import datetime
today = datetime.date.today()
CURRENT_DATE= "%s" % (today.isoformat())
CURRENT_DATE='2014-08-22'

def Print (field):
        return str(field)


def outputGenerator(desc,metric):
	print ""
        print desc
        for item in metric:
                print (" ".join([Print(field) for field in item]))


def formatString(stringToFormat):
	return stringToFormat.replace('CURRENT_DATE','%s' %CURRENT_DATE)
