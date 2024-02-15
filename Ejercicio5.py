
import sys

def descomponer_direccion_ip(ip):
    octetos = ip.split('.')
    for octeto in octetos:
        print(octeto)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Uso: python descomponer_ip.py <direccion_ip>')
        sys.exit(1)
    
    direccion_ip = sys.argv[1]
    descomponer_direccion_ip(direccion_ip)
