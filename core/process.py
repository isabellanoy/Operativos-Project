# core/process.py

class Process:
    """
    Clase que representa un proceso en el sistema.
    """
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

        # Estado actual (Nuevo, Listo, Ejecutando, Terminado)
        self.state = "Nuevo"

        # Atributos para métricas
        self.start_time = None
        self.completion_time = None
        self.remaining_time = burst_time  # Para Round Robin y prioridades con desalojo

    def __repr__(self):
        return (f"Process(pid={self.pid}, arrival={self.arrival_time}, "
                f"burst={self.burst_time}, priority={self.priority}, state={self.state})")
