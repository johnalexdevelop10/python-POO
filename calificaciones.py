class Estudiante:
    identificador: int
    nombre: str
    edad: int
    semestre: int
    notas: list
    
    def obtener_promedio(self):
        pass
    def ver_info(self):
        pass
    estudiantes:list[Estudiante]=[]
    
    while(True):
          op = int(input(""" escoje 1.ingresar datos 2.ver promedio estudiante 3. 
                         ver info estudiante 0 salir"""))
          
          if op == 0:
              break
          
          if op ==1:
            identificador = input("ingrese ID")
            nombre = input("ingrese nombre:")
            edad = int(input("edad:"))
            semestre = float(input("semestre:"))
            print("ingrese notas estudiante")
            
            notas = []
            for i in range(3):
                notas.append(float(input(f"ingrese la nota{i+1}")))
            estudiante = Estudiante(nombre,edad,semestre,notas)
            estudiantes.append(estudiante)
            
          elif op ==2 or op==3:
              identificador = int(input("ingrese id:"))
              for estudiante in estudiantes:
                  if estudiante.identificador == identificador and op==2:
                      estudiante.obtener_promedio()
                  elif estudiante.identificador == identificador and op==3:
                      estudiante.ver_info()               
         
         
                      
          else:
              pass
      
        
            
                
                
        