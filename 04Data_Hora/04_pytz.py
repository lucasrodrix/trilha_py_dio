from datetime import datetime
import pytz # type: ignore

data1 = datetime.now(pytz.timezone('Europe/Oslo'))
data2 = datetime.now(pytz.timezone('America/Sao_Paulo'))
print(data1)
print(data2)