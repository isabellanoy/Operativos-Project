# core/metrics.py

def calculate_metrics(process_list):
    """
    Calcula las métricas de rendimiento por proceso y promedios.

    Args:
        process_list (list): Lista de objetos Process con tiempos de inicio y finalización.

    Returns:
        dict: Diccionario con métricas por proceso y promedios.
    """
    metrics_per_process = []
    total_turnaround = 0
    total_waiting = 0
    total_response = 0

    for p in process_list:
        turnaround = p.completion_time - p.arrival_time
        waiting = turnaround - p.burst_time
        response = p.start_time - p.arrival_time

        metrics_per_process.append({
            "pid": p.pid,
            "arrival_time": p.arrival_time,
            "burst_time": p.burst_time,
            "start_time": p.start_time,
            "completion_time": p.completion_time,
            "turnaround_time": turnaround,
            "waiting_time": waiting,
            "response_time": response,
            "priority": p.priority
        })

        total_turnaround += turnaround
        total_waiting += waiting
        total_response += response

    n = len(process_list)
    avg_turnaround = total_turnaround / n
    avg_waiting = total_waiting / n
    avg_response = total_response / n

    return {
        "per_process": metrics_per_process,
        "averages": {
            "average_turnaround_time": avg_turnaround,
            "average_waiting_time": avg_waiting,
            "average_response_time": avg_response
        }
    }
