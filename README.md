vea ñero, para instalar este repositorio simplemente instala Python 3.12
No la version 3.13 o arriba de ella. LA 3.12 para que tenga compatibilidad con la targeta grafica por si las moscas. 
--> https://www.python.org/downloads/release/python-3120/
(asegurate de marcar la opción de -Add to Path- mientras la instalación)
No importa si tenías un python distinto antes. Se pueden tener varias versiones simultaneamente.

Posteriormente, para preparar el programa, necesitamos crear un entorno virtual de Python para que no haya conflictos en tu pc y descargar ciertas librerías. Para hacerlo ejecuta el archivo install.bat haciendo doble click sobre él o en la terminal escribiendo:

    .\install.bat

Tras hacer eso, se creará el entorno virtual con todas las dependencias y se activará automáticamente (esto ultimo es importante)
Si por alguna razón ya creaste el entorno virtual y vez la carpeta "env312" pero crees que no estás dentro del entorno, ejecuta en la terminal:

    .\env312\Scripts\activate

y ahora podrás ejecutar el programa!

---

Para entrenar el modelo, ejecuta: 
    
    training.py

en ese archivo puedes modificar la cantidad de pasos 'TOTAL_TIMESTEPS' que determina qué tanto entrenará. Generalmente lo dejo por el millón (a mayor entrenada esté la IA, más demorarán los timesteps pues, el juego tenderá a durar mas porque la serpiente será menos propensa a perder)
En este modo, el juego no se ve. Solo unos logs de stable_baseline3

Para probar el modelo que ya se entrenó, ejecuta:

    model.py


Y YA mi sow
