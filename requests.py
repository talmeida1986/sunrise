import requests
from datetime import datetime
import pytz

# Coordenadas para Itaguaí - Rio de Janeiro
latitude = -22.8522
longitude = -43.7753

# Fazer uma solicitação à API Sunrise-Sunset
url = f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&date=today&formatted=0"
response = requests.get(url)
data = response.json()

# Obter os tempos de nascer e pôr do sol em UTC
sunrise_utc = datetime.strptime(data['results']['sunrise'], '%Y-%m-%dT%H:%M:%S+00:00')
sunset_utc = datetime.strptime(data['results']['sunset'], '%Y-%m-%dT%H:%M:%S+00:00')

# Converter os tempos para o fuso horário de São Paulo
saopaulo_timezone = pytz.timezone('America/Sao_Paulo')
sunrise_saopaulo = sunrise_utc.replace(tzinfo=pytz.utc).astimezone(saopaulo_timezone)
sunset_saopaulo = sunset_utc.replace(tzinfo=pytz.utc).astimezone(saopaulo_timezone)

# Imprimir os tempos de nascer e pôr do sol em Itaguaí - Rio de Janeiro
print(f"Nascer do Sol em Itaguaí: {sunrise_saopaulo.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Pôr do Sol em Itaguaí: {sunset_saopaulo.strftime('%Y-%m-%d %H:%M:%S')}")

# Calcular o horário de nascer do sol em Itaguaí - Rio de Janeiro
horario_nascer_do_sol = sunrise_saopaulo.strftime('%H:%M:%S')
print(f"Horário de Nascer do Sol em Itaguaí: {horario_nascer_do_sol}")
