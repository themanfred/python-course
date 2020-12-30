from pathlib import Path

try:
    f = open(Path.home() / 'texto.txt')
    f.write('la casa')
except:
    print('No se bro')
finally:
    print('Valgo verga')
    f.close()