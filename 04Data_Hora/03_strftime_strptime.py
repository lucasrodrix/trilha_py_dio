from datetime import datetime

dataHoraAtual = datetime.now()
dataHoraStr = '2024-05-29 12:00'

mascaraPtBr = '%d/%m/%Y %H:%M'
mascaraEn = '%Y-%m-%d %H:%M'

print(dataHoraAtual.strftime(mascaraPtBr))
print(datetime.strptime(dataHoraStr, mascaraEn))
