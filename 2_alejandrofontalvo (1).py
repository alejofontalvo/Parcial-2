import unittest
class Personal:
  def __init__(self) -> None: #Esta clase nos permite recoger los datos de nuestro 
    self.NombresEmpleados = []
    self.EdadEmpleados = []
    self.IDEmpleados = []

  def Registrar_empleado(self,camion,Empresa):
    i = 0
    print("           Recuerda Agregar al Conductor y los dos Ayudantes            ")
    for i in range(3):
     if(i == 0):
      print("-----------------------------------------------------------------------")
      c = input(f"Digita el ID del Conductor del camion con ID {camion.ID_Camion} = ")
      while not c.isdigit():  # Verifica si el valor ingresado es un número entero
                c = input("ID inválida. Por favor, ingresa un ID entero = ")
      print("-----------------------------------------------------------------------")
      n = input(f"Digita el Nombre del Conductor del camion con ID {camion.ID_Camion} = ")
      print("-----------------------------------------------------------------------")
      E = input(f"Digita la Edad del Conductor del camion con ID {camion.ID_Camion} = ")
      while not E.isdigit():  # Verifica si el valor ingresado es un número entero
                E = input("Edad inválida. Por favor, ingresa un número entero = ")
      print("-----------------------------------------------------------------------")
      Empresa.Lista_Conductor.append(c)
      self.NombresEmpleados.append(n)
      self.EdadEmpleados.append(E)
      self.IDEmpleados.append(c)
     elif (i == 1):
      d = input(f"Digita el ID del Acompañante #1 del camion con ID {camion.ID_Camion} = ")
      while not d.isdigit():  # Verifica si el valor ingresado es un número entero
                d = input("ID inválida. Por favor, ingresa un ID entero = ")
      print("-----------------------------------------------------------------------")
      n1 = input(f"Digita el Nombre del Acompañante #1 del camion con ID {camion.ID_Camion} = ")
      print("-----------------------------------------------------------------------")
      E1 = input(f"Digita la Edad del Acompañante #1 del camion con ID {camion.ID_Camion} = ")
      while not E1.isdigit():  
                E1 = input("Edad inválida. Por favor, ingresa un número entero = ")
      print("-----------------------------------------------------------------------")
      Empresa.Lista_Acompañantes.append(d)
      self.NombresEmpleados.append(n1)
      self.EdadEmpleados.append(E1)
      self.IDEmpleados.append(d)
     elif (i == 2):
      e = input(f"Digita el ID del Acompañante #2 del camion con ID {camion.ID_Camion} = ")
      while not e.isdigit():  # Verifica si el valor ingresado es un número entero
                e = input("ID inválida. Por favor, ingresa un ID entero = ")
      print("-----------------------------------------------------------------------")
      n2 = input(f"Digita el Nombre del Acompañante #2 del camion con ID {camion.ID_Camion} = ")
      print("-----------------------------------------------------------------------")
      E2 = input(f"Digita la Edad del Acompañante #2 del camion con ID {camion.ID_Camion} = ")
      while not E2.isdigit():  # Verifica si el valor ingresado es un número entero
                E2 = input("Edad inválida. Por favor, ingresa un número entero = ")
      print("-----------------------------------------------------------------------")
      Empresa.Lista_Acompañantes.append(e)
      self.NombresEmpleados.append(n2)
      self.EdadEmpleados.append(E2)
      self.IDEmpleados.append(e)


class Camiones: 
    def __init__(self, Modelo_Camion: str, ID_Camion: str) -> None:
     self.Nombre = Modelo_Camion
     self.ID_Camion = ID_Camion
     self.estrategia_recoleccion = None

    def Crear_Camion(self,Empresa,camion)-> None:
      Empresa.Lista_Camiones.append(self.ID_Camion)
      b = Personal()
      b.Registrar_empleado(camion,Empresa)

    def establecer_estrategia_recoleccion(self, estrategia_recoleccion):
        self.estrategia_recoleccion = estrategia_recoleccion

    def realizar_recoleccion(self, residuos,Empresa, Geo):
        if self.estrategia_recoleccion:
            self.estrategia_recoleccion.realizar_recoleccion(residuos,Empresa,Geo)
        else:
            print("No se ha establecido una estrategia de recolección")
     

class TrashCity:
    __instance = None

    @staticmethod
    def getInstance():
        if TrashCity.__instance is None:
            TrashCity()
        return TrashCity.__instance
    
    def __init__(self):
      if TrashCity.__instance is not None:
            raise Exception("This class is a Singleton!")
      else:
       self.Lista_Conductor = []
       self.Lista_Acompañantes = []
       self.Lista_Camiones = []
       self.ResiduosV = [0]
       self.ResiduosP = [0]
       self.ResiduosM = [0]
       self.TotalVR = 0
       self.TotalPR = 0
       self.TotalMR = 0
    
    def Mostrar_Empleados(self):
      for cadena in self.Lista_Conductor:
        print("------------------------")
        print("ID de los Conductores: ", cadena)
        print("------------------------")

    def Mostrar_Camion(self):
      for cadena in self.Lista_Camiones:
        print("------------------------")
        print("ID del camión: ", cadena)
        print("------------------------")



    def Contar_Residuos_Vidrio_Total(self,Geolocalizacion):
      if Geolocalizacion.Turno == True:
        for cadena in self.ResiduosV:
         self.TotalVR = self.TotalVR + cadena
      else:
        print("NO HA TERMINADO EL TURNO")
      self.ResiduosV.append(self.TotalVR)
      print("//////////////////////////////////////////////////////////////") 
      print("             TOTAL             ")
      print("El total de residuos recogidos en el día ", Geolocalizacion.Dia ," es:", self.TotalVR, " Residuos de Vidrio" )
      print("//////////////////////////////////////////////////////////////")

    def Contar_Residuos_Papel_Total(self,Geolocalizacion):
      if Geolocalizacion.Turno == True:
        for cadena in self.ResiduosP:
         self.TotalPR = self.TotalPR + cadena
      else:
        print("NO HA TERMINADO EL TURNO")
      self.ResiduosP.append(self.TotalPR)
      print("//////////////////////////////////////////////////////////////") 
      print("             TOTAL             ")
      print("El total de residuos recogidos en el día ", Geolocalizacion.Dia ," es:", self.TotalPR, " Residuos de papel" )
      print("//////////////////////////////////////////////////////////////")
     
    def Contar_Residuos_Metal_Total(self,Geolocalizacion):
      if Geolocalizacion.Turno == True:
        for cadena in self.ResiduosM:
         self.TotalMR = self.TotalMR + cadena
      else:
        print("NO HA TERMINADO EL TURNO")
      self.ResiduosM.append(self.TotalMR)
      print("//////////////////////////////////////////////////////////////") 
      print("             TOTAL             ")
      print("El total de residuos recogidos en el día ", Geolocalizacion.Dia ," es:", self.TotalMR, " Residuos de Metal" )
      print("//////////////////////////////////////////////////////////////")

class Geolocalizacion:
   def __init__(self,Latitud, Longitud,Dia):
     self.Turno = False
     self.Latitud = Latitud
     self.Longitud = Longitud
     self.Dia = Dia
    
   def Acabar_turno(self):
      self.Turno = True
      print("//////////////////")
      print("Hora de descansar") 
      print("//////////////////")

class EstrategiaRecoleccion:
    def realizar_recoleccion(self, residuos,Empresa,Geo):
        pass

class EstrategiaRecoleccionVidrio(EstrategiaRecoleccion):
    
    def realizar_recoleccion(self,ResiduosV,Empresa,Geo):
      print("Realizando recolección de residuos de vidiro...")
      print("/////////////////////////////////////////////////////////////////////////////////////////")
      print("                                RECOLECCION                                              ")
      print("El camion ha recolectado ", ResiduosV, "Residuos de VIDRIO en la Latitud ", Geo.Latitud," y Longitud ",Geo.Longitud)
      print("/////////////////////////////////////////////////////////////////////////////////////////")
      Empresa.ResiduosV.append(ResiduosV)

class EstrategiaRecoleccionPapel(EstrategiaRecoleccion):
  
    def realizar_recoleccion(self,ResiduosP,Empresa,Geo):
      print("Realizando recolección de residuos de Papel...")
      print("/////////////////////////////////////////////////////////////////////////////////////////")
      print("            RECOLECCION            ")
      print("El camion ha recolectado ", ResiduosP, "Residuos de PAPEL en la Latitud ", Geo.Latitud," y Longitud ",Geo.Longitud)
      print("/////////////////////////////////////////////////////////////////////////////////////////")
      Empresa.ResiduosP.append(ResiduosP)


class EstrategiaRecoleccionMetal(EstrategiaRecoleccion):
   def realizar_recoleccion(self,ResiduosM,Empresa,Geo):
      print("Realizando recolección de residuos de Metal...")
      print("/////////////////////////////////////////////////////////////////////////////////////////")
      print("            RECOLECCION            ")
      print("El camion ha recolectado ", ResiduosM, "Residuos de METAL en la Latitud ", Geo.Latitud," y Longitud ",Geo.Longitud)
      print("/////////////////////////////////////////////////////////////////////////////////////////")
      Empresa.ResiduosM.append(ResiduosM) 

class TrashCityTests(unittest.TestCase):

    def test_Contar_Residuos_Vidrio_Total(self):
        TC = TrashCity()
        GEO = Geolocalizacion(407128, 740060, "19/05/2023")
        
        
        GEO.Turno = True
        
        TC.ResiduosV = [10, 15, 20]

        TC.Contar_Residuos_Vidrio_Total(GEO)

       
        self.assertEqual(TC.TotalVR, 45)  
        
        
        self.assertEqual(TC.ResiduosV[-1], 45) 
    
    def test_Contar_Residuos_Papel_Total(self):
        TC = TrashCity()
        GEO = Geolocalizacion(997128, 234, "29/07/2022")
        
        
        GEO.Turno = True
        
        TC.ResiduosP = [90, 200, 520]

        
        TC.Contar_Residuos_Papel_Total(GEO)

        
        self.assertEqual(TC.TotalPR, 810)  
        
        
        self.assertEqual(TC.ResiduosP[-1], 810) 
         
    def test_Contar_Residuos_Metal_Total(self):
        TC = TrashCity()
        GEO = Geolocalizacion(943445, 234232, "12/07/2022")
        
        
        GEO.Turno = True
        
        TC.ResiduosM = [1000, 1000, 1000]

        
        TC.Contar_Residuos_Metal_Total(GEO)

        
        self.assertEqual(TC.TotalMR, 3000)  
        
       
        self.assertEqual(TC.ResiduosM[-1], 3000)  
    

      
print("--------------------------------------------------")
print("-                                                -")
print("-                                                -")
print("-                                                -")
print("-                ~ TRASHCITY ~                   -")
print("-                        BY: Alejandro Fontalvo  -")
print("-                                                -")
print("-                                                -")
print("--------------------------------------------------")
P = Personal()
E = TrashCity()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Sean bienvenido a Trashcity, una comunidad de acopio y reciclaje")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("-----------------------------------------------------------------")
op0 = int(input("""Desea iniciar el programa 
         1. Si
         2. No                              
           = """))
print("-----------------------------------------------------------------")
while op0 != 1 and op0 != 2:
  print("-----------------------------------------------------------------")
  op0 = int(input("""ERROR: Solo puedes digitar 1 o 2
                  Desea iniciar el programa
                  1. Si
                  2. No                              
                      = """))
  print("-----------------------------------------------------------------")
while op0 == 1:
    op = int(input("""Desea Registrar un Camión de Recolección 
         1. Si
         2. No                              
           = """))
    print("-----------------------------------------------------------------")

    while op != 1 and op != 2:
       print("-----------------------------------------------------------------")
       op = int(input("""ERROR: Solo puedes digitar 1 o 2
                  Desea Registrar un Camión de Recolección 
                  1. Si
                  2. No                              
                      = """))
       print("-----------------------------------------------------------------")

    if op == 1:
        Modelo = str(input("Digite el Modelo del camión = "))
        ID = input("Digite el ID del camión = ")
        while not ID.isdigit():  
           ID = input("ID inválida. Por favor, ingresa un ID entero = ")
           print("-----------------------------------------------------------------")
        C = Camiones(Modelo,ID)
        C.Crear_Camion(E,C)
        E.Mostrar_Camion()
        E.Mostrar_Empleados()
        op2 = int(input(""" Desea Agregar Residuos de un Punto Geográfico 
                               1. Si
                               2. No                              
                                = """))
        print("-----------------------------------------------------------------")
        while op2 != 1 and op2 != 2:
              print("-----------------------------------------------------------------")
              op2 = int(input("""ERROR: Solo puedes digitar 1 o 2
                  Desea Agregar Residuos de un Punto Geográfico
                  1. Si
                  2. No                              
                      = """))
              print("-----------------------------------------------------------------")
        while(op2 == 1):
             print("-----------------------------------------------------------------")
             lon = input("Digite la Longitud en donde se recogen los residuos = ")
             lat = input("Digite la Latitud en donde se recogen los residuos = ")
             dia = input("Digite la fecha en que se recogen los residuos = ")
             G = Geolocalizacion(lon,lat,dia)
             print("-----------------------------------------------------------------")
             vid = int(input("Digite el número de residuos de vidrio = "))
             pap = int(input("Digite el número de residuos de papel = "))
             met = int(input("Digite el número de residuos de metal = "))
             C.establecer_estrategia_recoleccion(EstrategiaRecoleccionVidrio())
             C.realizar_recoleccion(vid,E,G)
             C.establecer_estrategia_recoleccion(EstrategiaRecoleccionPapel())
             C.realizar_recoleccion(pap,E,G)
             C.establecer_estrategia_recoleccion(EstrategiaRecoleccionMetal())
             C.realizar_recoleccion(met,E,G)
             op2 = int(input(""" Desea agregar más Residuos de un Punto Geográfico 
                                 1. Si
                                 2. No                              
                                  = """))
             print("-----------------------------------------------------------------")
             while op2 != 1 and op2 != 2:
                print("-----------------------------------------------------------------")
                op2 = int(input("""ERROR: Solo puedes digitar 1 o 2
                  Desea Agregar Residuos de un Punto Geográfico
                     1. Si
                     2. No                              
                                = """))
        print("Culminó el turno ejercido")
        G.Acabar_turno()
        E.Contar_Residuos_Vidrio_Total(G)
        E.Contar_Residuos_Papel_Total(G)
        E.Contar_Residuos_Metal_Total(G)
        print("-----------------------------------------------------------------")
    else:
      op0 = 0
    op0 = int(input("""Desea seguir el programa 
         1. Si
         2. No                              
           = """))
    print("-----------------------------------------------------------------")
    while op0 != 1 and op0 != 2:
     print("-----------------------------------------------------------------")
     op0 = int(input("""ERROR: Solo puedes digitar 1 o 2
                  Desea seguir el programa
                  1. Si
                  2. No                              
                      = """))
     print("-----------------------------------------------------------------")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                     Ha Cerrado Trashcity                        ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
if __name__ == "__main__":
    unittest.main()
