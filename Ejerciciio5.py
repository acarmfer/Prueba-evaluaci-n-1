import ipaddress

def descomponer_direccion_ip(ip):
    octetos = ip.split('.')
    return octetos

def validar_direccion_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def pedir_direccion_ip():
    while True:
        ip = input("Introduce una dirección IP: ")
        if validar_direccion_ip(ip):
            return ip
        else:
            print("Dirección IP inválida. Inténtalo de nuevo.")

# Pedir la dirección IP al usuario
ip = pedir_direccion_ip()

# Descomponer la dirección IP en sus octetos
octetos = descomponer_direccion_ip(ip)

# Mostrar cada octeto línea por línea
for octeto in octetos:
    print(octeto)
