from datetime import datetime, timedelta, timezone

data1 = datetime.now(timezone(timedelta(hours=+2),'OSL'))
data2 = datetime.now(timezone(timedelta(hours=-3),'BRT'))
print(data1)
print(data2)