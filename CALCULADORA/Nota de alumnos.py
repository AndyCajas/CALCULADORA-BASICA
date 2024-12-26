import tkinter as tk
from tkinter import messagebox

class Alumno:
    def __init__(self, dni, apellidos, nombre, nota):
        self.dni = dni
        self.apellidos = apellidos
        self.nombre = nombre
        self.nota = nota
        self.calificacion = self.calcular_calificacion()

    def calcular_calificacion(self):
        if self.nota < 5:
            return "SS"
        elif 5 <= self.nota < 7:
            return "AP"
        elif 7 <= self.nota < 9:
            return "NT"
        else:
            return "SB"

class GestionCalificaciones:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Calificaciones")
        self.alumnos = {}

        # Cambiar el color de fondo de la ventana principal a negro
        self.root.configure(bg="black")

        # Widgets principales
        self.dni_label = tk.Label(root, text="DNI:", bg="black", fg="white")
        self.dni_label.grid(row=0, column=0, padx=10, pady=10)
        self.dni_entry = tk.Entry(root)
        self.dni_entry.grid(row=0, column=1, padx=10, pady=10)

        self.nombre_label = tk.Label(root, text="Nombre:", bg="black", fg="white")
        self.nombre_label.grid(row=1, column=0, padx=10, pady=10)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=1, column=1, padx=10, pady=10)

        self.apellidos_label = tk.Label(root, text="Apellidos:", bg="black", fg="white")
        self.apellidos_label.grid(row=2, column=0, padx=10, pady=10)
        self.apellidos_entry = tk.Entry(root)
        self.apellidos_entry.grid(row=2, column=1, padx=10, pady=10)

        self.nota_label = tk.Label(root, text="Nota:", bg="black", fg="white")
        self.nota_label.grid(row=3, column=0, padx=10, pady=10)
        self.nota_entry = tk.Entry(root)
        self.nota_entry.grid(row=3, column=1, padx=10, pady=10)

        # Botones de acción a la izquierda
        self.introducir_button = tk.Button(root, text="Introducir Alumno", bg="lightblue", command=self.introducir_alumno)
        self.introducir_button.grid(row=4, column=0, padx=10, pady=10)

        self.mostrar_button = tk.Button(root, text="Mostrar Alumnos", bg="lightgreen", command=self.mostrar_alumnos)
        self.mostrar_button.grid(row=5, column=0, padx=10, pady=10)

        self.eliminar_button = tk.Button(root, text="Eliminar Alumno", bg="salmon", command=self.eliminar_alumno)
        self.eliminar_button.grid(row=6, column=0, padx=10, pady=10)

        self.consultar_button = tk.Button(root, text="Consultar Alumno", bg="lightyellow", command=self.consultar_alumno)
        self.consultar_button.grid(row=7, column=0, padx=10, pady=10)

        # Botones de acción a la derecha
        self.modificar_nota_button = tk.Button(root, text="Modificar Nota", bg="lightcoral", command=self.modificar_nota)
        self.modificar_nota_button.grid(row=4, column=2, padx=10, pady=10)

        self.suspensos_button = tk.Button(root, text="Mostrar Suspensos", bg="orange", command=self.mostrar_suspensos)
        self.suspensos_button.grid(row=5, column=2, padx=10, pady=10)

        self.aprobados_button = tk.Button(root, text="Mostrar Aprobados", bg="lightcyan", command=self.mostrar_aprobados)
        self.aprobados_button.grid(row=6, column=2, padx=10, pady=10)

        self.mh_button = tk.Button(root, text="Candidatos a MH", bg="plum", command=self.mostrar_mh)
        self.mh_button.grid(row=7, column=2, padx=10, pady=10)

    def introducir_alumno(self):
        dni = self.dni_entry.get()
        nombre = self.nombre_entry.get()
        apellidos = self.apellidos_entry.get()
        try:
            nota = float(self.nota_entry.get())
        except ValueError:
            messagebox.showerror("Error", "La nota debe ser un número válido.")
            return

        if dni in self.alumnos:
            messagebox.showerror("Error", "Ya existe un alumno con este DNI.")
        else:
            self.alumnos[dni] = Alumno(dni, apellidos, nombre, nota)
            messagebox.showinfo("Éxito", "Alumno introducido correctamente.")

    def mostrar_alumnos(self):
        if not self.alumnos:
            messagebox.showinfo("Información", "No hay alumnos registrados.")
            return

        info = ""
        for alumno in self.alumnos.values():
            info += f"{alumno.dni} {alumno.apellidos}, {alumno.nombre} {alumno.nota} {alumno.calificacion}\n"
        self.mostrar_info(info)

    def eliminar_alumno(self):
        dni = self.dni_entry.get()
        if dni in self.alumnos:
            del self.alumnos[dni]
            messagebox.showinfo("Éxito", "Alumno eliminado correctamente.")
        else:
            messagebox.showerror("Error", "No se encontró un alumno con ese DNI.")

    def consultar_alumno(self):
        dni = self.dni_entry.get()
        if dni in self.alumnos:
            alumno = self.alumnos[dni]
            messagebox.showinfo("Información", f"DNI: {alumno.dni}\nNombre: {alumno.nombre}\nApellidos: {alumno.apellidos}\nNota: {alumno.nota}\nCalificación: {alumno.calificacion}")
        else:
            messagebox.showerror("Error", "No se encontró un alumno con ese DNI.")

    def modificar_nota(self):
        dni = self.dni_entry.get()
        if dni in self.alumnos:
            try:
                nueva_nota = float(self.nota_entry.get())
            except ValueError:
                messagebox.showerror("Error", "La nota debe ser un número válido.")
                return

            alumno = self.alumnos[dni]
            alumno.nota = nueva_nota
            alumno.calificacion = alumno.calcular_calificacion()
            messagebox.showinfo("Éxito", "Nota modificada correctamente.")
        else:
            messagebox.showerror("Error", "No se encontró un alumno con ese DNI.")

    def mostrar_suspensos(self):
        suspensos = [alumno for alumno in self.alumnos.values() if alumno.nota < 5]
        if not suspensos:
            messagebox.showinfo("Información", "No hay alumnos suspensos.")
            return

        info = "\n".join([f"{alumno.dni} {alumno.apellidos}, {alumno.nombre} {alumno.nota} {alumno.calificacion}" for alumno in suspensos])
        self.mostrar_info(info)

    def mostrar_aprobados(self):
        aprobados = [alumno for alumno in self.alumnos.values() if alumno.nota >= 5]
        if not aprobados:
            messagebox.showinfo("Información", "No hay alumnos aprobados.")
            return

        info = "\n".join([f"{alumno.dni} {alumno.apellidos}, {alumno.nombre} {alumno.nota} {alumno.calificacion}" for alumno in aprobados])
        self.mostrar_info(info)

    def mostrar_mh(self):
        mh = [alumno for alumno in self.alumnos.values() if alumno.nota == 10]
        if not mh:
            messagebox.showinfo("Información", "No hay candidatos a matrícula de honor.")
            return

        info = "\n".join([f"{alumno.dni} {alumno.apellidos}, {alumno.nombre} {alumno.nota} {alumno.calificacion}" for alumno in mh])
        self.mostrar_info(info)

    def mostrar_info(self, info):
        info_window = tk.Toplevel(self.root)
        info_window.title("Información")
        text = tk.Text(info_window, wrap="word")
        text.insert("1.0", info)
        text.config(state="disabled")
        text.pack()

# Iniciar la aplicación
root = tk.Tk()
root.geometry("400x400")  # Cambiar el tamaño de la ventana aquí
app = GestionCalificaciones(root)
root.mainloop()

