# algorithms/fcfs.py

def fcfs(process_list):
    """
    Simula el algoritmo FCFS (First Come, First Served).

    Args:
        process_list (list): Lista de objetos Process.

    Returns:
        list: Lista de procesos con tiempos de inicio y finalización actualizados.
    """
    # Ordenar por tiempo de llegada
    processes = sorted(process_list, key=lambda p: p.arrival_time)
    current_time = 0

    for process in processes:
        # Si el proceso llega después del tiempo actual, esperar
        if current_time < process.arrival_time:
            current_time = process.arrival_time

        process.start_time = current_time
        process.completion_time = current_time + process.burst_time
        process.remaining_time = 0
        process.state = "Terminado"

        current_time = process.completion_time

    return processes
