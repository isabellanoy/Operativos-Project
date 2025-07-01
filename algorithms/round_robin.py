# algorithms/round_robin.py

def round_robin(process_list, quantum):
    """
    Simula el algoritmo Round Robin.

    Args:
        process_list (list): Lista de objetos Process.
        quantum (int): Quantum de tiempo configurable.

    Returns:
        list: Lista de procesos con tiempos de inicio y finalización actualizados.
    """
    from collections import deque

    processes = sorted(process_list, key=lambda p: p.arrival_time)
    queue = deque()
    current_time = 0
    completed = []
    arrived = []

    while processes or queue:
        # Añadir procesos que llegan en este momento
        arrived = [p for p in processes if p.arrival_time <= current_time]
        for p in arrived:
            queue.append(p)
        processes = [p for p in processes if p not in arrived]

        if not queue:
            # Si no hay procesos en cola, avanzar al siguiente
            if processes:
                current_time = processes[0].arrival_time
                continue
            else:
                break

        process = queue.popleft()

        # Registrar el tiempo de inicio si es la primera vez que ejecuta
        if process.start_time is None:
            process.start_time = current_time

        # Ejecutar el proceso por un quantum o hasta que termine
        execution_time = min(quantum, process.remaining_time)
        current_time += execution_time
        process.remaining_time -= execution_time

        # Verificar si el proceso terminó
        if process.remaining_time == 0:
            process.completion_time = current_time
            process.state = "Terminado"
            completed.append(process)
        else:
            # Verificar si llegaron nuevos procesos durante esta ejecución
            arrived_during = [p for p in processes if p.arrival_time <= current_time]
            for p in arrived_during:
                queue.append(p)
            processes = [p for p in processes if p not in arrived_during]

            # Reagendar el proceso al final de la cola
            queue.append(process)

    return sorted(completed, key=lambda p: p.pid)

