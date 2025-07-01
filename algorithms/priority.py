# algorithms/priority.py

def priority_scheduling(process_list):
    """
    Simula el algoritmo de planificación por prioridades NO apropiativo.

    Args:
        process_list (list): Lista de objetos Process.

    Returns:
        list: Lista de procesos con tiempos de inicio y finalización actualizados.
    """
    processes = process_list.copy()
    completed = []
    current_time = 0

    while processes:
        # Filtrar procesos que hayan llegado
        available = [p for p in processes if p.arrival_time <= current_time]

        if not available:
            # Si no hay procesos disponibles, avanzar el reloj
            next_arrival = min(p.arrival_time for p in processes)
            current_time = next_arrival
            available = [p for p in processes if p.arrival_time <= current_time]

        # Seleccionar el proceso con la prioridad más alta (número más bajo)
        highest_priority = min(available, key=lambda p: p.priority)

        highest_priority.start_time = current_time
        highest_priority.completion_time = current_time + highest_priority.burst_time
        highest_priority.remaining_time = 0
        highest_priority.state = "Terminado"

        current_time = highest_priority.completion_time

        # Mover a completados
        completed.append(highest_priority)
        processes.remove(highest_priority)

    return completed
