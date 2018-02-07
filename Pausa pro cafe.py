import webbrowser
import time

total_paradas = 5 #Número total de paradas
cont_paradas = 0 #Contador das paradas

print("Programa iniciou as "+time.ctime()) #Mostra a hora que o programa iniciou
while(cont_paradas < total_paradas): #Loop "while" para rodar mais de uma vez o video
    time.sleep(2*60*60)  # Faz o programa esperar 2 horas
    webbrowser.open("https://www.youtube.com/watch?v=vCsi-lxW4yM")  # Abre o video no navegador
    cont_paradas+=1 # Contador conta mais uma volta

