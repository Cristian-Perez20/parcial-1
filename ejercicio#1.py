from datetime import datetime, timedelta

class Paciente:
    def __init__(self, nombre, motivo_consulta):
        self.nombre = nombre
        self.motivo_consulta = motivo_consulta
        self.fecha_consulta = None

class Secretaria:
    def __init__(self):
        self.pacientes = []
        self.agenda = {}

    def registrar_paciente(self, paciente):
        if paciente.nombre in self.agenda:
            print(f"{paciente.nombre} ya tiene una consulta programada.")
            self.enviar_a_sala_espera(paciente)
        else:
            print(f"Registrando a {paciente.nombre} para consulta.")
            self.pacientes.append(paciente)
            self.asignar_fecha_consulta(paciente)
    
    def asignar_fecha_consulta(self, paciente):
        fecha_actual = datetime.now()
        fecha_consulta = fecha_actual + timedelta(days=1)
        paciente.fecha_consulta = fecha_consulta
        self.agenda[paciente.nombre] = fecha_consulta
        print(f"Consulta asignada para {paciente.nombre} el {fecha_consulta.strftime('%Y-%m-%d %H:%M')}.")

    def enviar_a_sala_espera(self, paciente):
        print(f"{paciente.nombre} ha sido enviado a la sala de espera.")

class Consultorio:
    def __init__(self):
        self.secretaria = Secretaria()

    def llegada_paciente(self, nombre, motivo_consulta):
        paciente = Paciente(nombre, motivo_consulta)
        self.secretaria.registrar_paciente(paciente)

# Ejemplo de uso
consultorio = Consultorio()

# Pacientes llegando al consultorio
consultorio.llegada_paciente("Park Jimin", "Dolor de cabeza")
consultorio.llegada_paciente("Min Yoongi", "Chequeo general")
consultorio.llegada_paciente("Jeon JungKook", "Dolor de estómago")  # Jeon ya estaba registrado, va a sala de espera
