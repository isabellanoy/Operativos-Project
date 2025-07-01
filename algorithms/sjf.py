# algorithms/sjf.py

def sjf(process_list):
    """
    Simula el algoritmo SJF (Shortest Job First) NO apropiativo.

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
            # Si no hay disponibles, avanzar el tiempo al siguiente proceso que llegue
            next_arrival = min(p.arrival_time for p in processes)
            current_time = next_arrival
            available = [p for p in processes if p.arrival_time <= current_time]

        # Seleccionar el proceso con menor burst time
        shortest = min(available, key=lambda p: p.burst_time)

        shortest.start_time = current_time
        shortest.completion_time = current_time + shortest.burst_time
        shortest.remaining_time = 0
        shortest.state = "Terminado"

        current_time = shortest.completion_time

        # Moverlo a completados
        completed.append(shortest)
        processes.remove(shortest)

    return completed
