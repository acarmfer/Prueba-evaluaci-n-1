import argparse

def descomponer_direccion_ip(ip):
    # Dividir la dirección IP en sus octetos
    octetos = ip.split('.')
    
    # Mostrar cada octeto línea por línea
    for octeto in octetos:
        print(octeto)

# Configurar el parser de argumentos
parser = argparse.ArgumentParser(description='Descomponer una dirección IP en sus octetos.')
parser.add_argument('python Ejercicio5.py 192.168.1.1', type=str, help='La dirección IP que se va a descomponer.')

# Analizar los argumentos de la línea de comandos
args = parser.parse_args()

# Llamar a la función para descomponer la dirección IP
print("Descomposición de la dirección IP:")
descomponer_direccion_ip(args.direccion_ip)
