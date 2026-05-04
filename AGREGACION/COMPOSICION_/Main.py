def Main():
ed = Edificio("Torres UMSA", 500)

p = Parqueo(20, 10)
ed.adicionarParqueo(p)

d1 = Departamento(101, 1)
d2 = Departamento(102, 1)
d3 = Departamento(201, 2)

h1 = Habitacion("Dormitorio", 20)
h2 = Habitacion("Sala", 25)
h3 = Habitacion("Cocina", 15)

h4 = Habitacion("Dormitorio", 18)
h5 = Habitacion("Sala", 22)

h6 = Habitacion("Suite", 30)

h1.agregarMueble(Mueble("Cama", "Madera"))
h1.agregarMueble(Mueble("Mesa", "Metal"))

h2.agregarMueble(Mueble("Sofa", "Cuero"))

h6.agregarMueble(Mueble("TV", "Plastico"))
h6.agregarMueble(Mueble("Ropero", "Madera"))
h6.agregarMueble(Mueble("Mesa", "Vidrio"))


d1.agregarHabitacion(h1)
d1.agregarHabitacion(h2)
d1.agregarHabitacion(h3)

d2.agregarHabitacion(h4)
d2.agregarHabitacion(h5)

d3.agregarHabitacion(h6)

ed.agregarDepartamento(d1)
ed.agregarDepartamento(d2)
ed.agregarDepartamento(d3)
ed.mostrarMayorHabitacionesPiso(1)
ed.agregarMuebleDepartamento(102, 1, Mueble("Silla", "Madera"))
ed.mostrarDepartamentoMasMuebles()
ed.mostrarHabitacionMasMueblesPiso(1)
ed.eliminarDepartamentosPrimos()

print("\nDespués de eliminar departamentos primos:")
ed.mostrar()