    #Un resplandor y hace ¡BOOM! y digo, ains ya está aquí la guerra
      #  Como dice la señora del famoso meme (link), un día estalló la guerra.
       #  Haz un programa que, dado un número que se pasa por entrada,
       # haga una cuenta atrás y acabe con un ¡BOOM!.

#        Ejemplo de entrada:
 #       -----------------------------
   #             5

  #      Ejemplo de salida:
    #    -----------------------------
      #          5
     #   4
       # 3
        #2
        #1
#¡BOOM!*/
import time
temporizador = int(input("¿Cuanto tiempo quieres para morir?\n"))
print("Empieza la cuenta atrás")
for i in range(temporizador, 0,-1):
    time.sleep(1)
    print(i)
print("¡BOOM!")