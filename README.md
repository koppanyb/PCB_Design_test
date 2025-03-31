# NUCLEO-F091RC fejlesztőpanelen tesztelt PCB-Design tesztfeladat

A forráskód megtekinthető a `main/STM32/PCB_DESIGN_teszt` mappában,  
a lefordított bináris állomány pedig a `main/STM32` könyvtárban található.

## Tesztelési szempontok

- **Stresszteszt**: A lehető leggyorsabban küldjük a LED kapcsolási parancsokat.  
- **Tetszőleges adatkezelés**: A rendszernek akkor is megfelelően kell értelmeznie a kapcsolási parancsokat,  
  ha nem értelmezhető tartalmú vagy méretű kódszavakat küldünk.
 ## Eredmény

A tesztelés alapján a parancsok fogadása és feldolgozása az elvártaknak megfelelően működnek.
