vea ñero, para instalar este repositorio simplemente instala Python 3.12
No la version 3.13 o arriba de ella. LA 3.12 para que tenga compatibilidad con la targeta grafica por si las moscas. 
--> https://www.python.org/downloads/release/python-3120/
(asegurate de marcar la opción de -Add to Path- mientras la instalación)

Para entrenar el modelo, ejecuta: 
    
    training.py

en ese archivo puedes modificar la cantidad de pasos 'total_timesteps' que determina qué tanto entrenará. Generalmente lo dejo por el millón (a mayor entrenada esté la IA, más demorarán los timesteps pues, el juego tenderá a durar mas)
En este modo, el juego no se ve. Solo unos logs de stable_baseline3

Para probar el modelo que ya se entrenó, ejecuta:

    model.py


Y YA mi sow
