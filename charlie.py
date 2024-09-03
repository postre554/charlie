import time
import os




def pause_with_message(message):
    os.system('clear')  # limpiamos la pantalla. antes de ciclo for
    print(message)
    input("\nPresiona cualquier tecla para continuar...")


frames = [
    """
            _._
          .'   `.
    ]     |     |
         "======="
          $ ^ ^ $ 
          `  #  '
           `._.'
        _.'< ' >'-._
      .'    \\ /     '
    """,
    """
             _._
           .'   `.
           |     |  ' 
          "======="
           $ ^ ^ $ 
           `  #  '
            `._.'
         _.'< ' >'-._
       .'    \\ /     '
    """,
    """
           ;  _._
            .'   `.
            |     |
           "======="
            $ ^ ^ $ 
      -     `  #  '
             `._.'
          _.'< ' >'-._
        .'    \\ /     '
    """,
    """
               _._
             .'   `.
             |     |
            "======="
             $ ^ ^ $ 
             `  #  '
              `._.'
           _.'< ' >'-._
         .'    \\ /     '
    """,
    """
                _._
              .'   `.
              |     |
             "======="
              $ ^ ^ $ 
              `  #  '
               `._.'
            _.'< ' >'-._
          .'    \\ /     '
    """,
    """

                _._
              .'   `.
              |     |
             "======="
              $ ^ ^ $ 
              `  #  '
               `._.'
            _.'< ' >'-._
          .'    \\ /     '
           G
    """,
    """
                _._
              .'   `.
              |     |
             "======="
              $ ^ ^ $ 
              `  #  '
               `._.'
            _.'< ' >'-._
          .'    \\ /     '
           GR
    """,
    """
                _._
              .'   `.
              |     |
             "======="
              $ ^ ^ $ 
              `  #  '
               `._.'
            _.'< ' >'-._
          .'    \\ /     '
           GRU
    """,
    """
                _._
              .'   `.
              |     |
             "======="
              $ ^ ^ $ 
              `  #  '
               `._.'
            _.'< ' >'-._
          .'    \\ /     '
           GRUP
    """,
    """
                _._
              .'   `.
              |     |
             "======="
              $ ^ ^ $ 
              `  #  '
               `._.'
            _.'< ' >'-._
          .'    \\ /     '
           GRUPO 1
    """,
    """
                _._
              .'   `.
              |     |
             "======="
              $ - - $ 
              `  #  '
               `._.'
            _.'< ' >'-._
          .'    \\ /     '
           GRUPO 1
    """,
    """
                _._
              .'   `.
              |     |
             "======="
              $ + + $ 
              `  #  '
               `._.'
            _.'< ' >'-._
          .'    \\ /     '
           GRUPO 1
    """,
    """
                _._
              .'   `.
              |     |
             "======="
              $ - - $ 
              `  #  '
               `._.'
            _.'< ' >'-._
          .'    \\ /     '
           GRUPO 1 PYTHON
    """
]

# Función para mostrar la animación
def animate(frames, repeat=6, delay=0.2):

    pause_with_message("Esta secuencia es un tributo a Charlie Chaplin, creado por Grupo 1")

    for _ in range(repeat):  # Repetimos la animación varias veces, y por cada ciclo limpiamos la pantalla
        for frame in frames:
            os.system('clear')  # Limpiamos la pantalla (en Windows usar 'cls')
            print(frame)
            time.sleep(delay)

# Ejecutamos la animación
animate(frames)

