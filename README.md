# Prueba para tutor de Python para Kodland

## Objetivo

El proyecto es una implementación del juego [Asteroids](https://es.wikipedia.org/wiki/Asteroids).  
Muestra un código bien estructurado con la intención de ser didáctico y fácil de ser explicado.

## Instalación y ejecución

Se necesita Python3 con [Pygame](https://www.pygame.org/) instalado, junto con otras dependencias que figuren en `requirements.txt`.  
Se puede usar un venv de Python:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Controles

Se mueve adelante y atrás con W y S. Y con A y D se rota la nave.  
Presionando ESCAPE se puede pausar el juego.  
Se consiguen puntos esquivando a los asteroides por la mayor cantidad de tiempo posible.
