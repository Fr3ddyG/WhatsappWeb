# Programa para enviar mensagens automaticamente via WhatsApp Web

import pywhatkit as kit
import time
import pyautogui as auto

print("O programa se iniciou")
# Definir o número do destinatário e a mensagem
def enviar_mensagem(numero, mensagem):
    try:
        print(f"Enviando mensagem para {numero}...")
        
        kit.sendwhatmsg_instantly(numero, mensagem, wait_time=15, tab_close=True)  

        time.sleep(10)
        auto.press("enter")

        print(f"Mensagem enviada com sucesso para {numero}!")

    except Exception as e:
        print(f"Ocorreu um erro ao enviar a mensagem: {e}")

if __name__ == "__main__":
    lista_numeros = [
        "+5599999999999"
    ]

    mensagem = """
    Olá, esta é uma mensagem automática enviada via WhatsApp Web!

    """
print("Iniciando o envio de mensagens...")

for numero in lista_numeros:
    enviar_mensagem(numero, mensagem)
    time.sleep(5)  # Pausa entre envios para evitar bloqueios

