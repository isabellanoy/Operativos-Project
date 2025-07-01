# ui/ui_main.py

import tkinter as tk
from tkinter import ttk, messagebox

from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.round_robin import round_robin
from algorithms.priority import priority_scheduling
from core.metrics import calculate_metrics
from core.process import Process


class SchedulerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Planificación de CPU")

        # Lista de procesos
        self.processes = []

        # Configuración de algoritmo
        self.selected_algorithm = tk.StringVar()
        self.quantum_value = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky="NSEW")

        # Tabla de procesos
        self.tree = ttk.Treeview(main_frame, columns=("Arrival", "Burst", "Priority"), show="headings")
        self.tree.heading("Arrival", text="Tiempo de llegada")
        self.tree.heading("Burst", text="Rafaga")
        self.tree.heading("Priority", text="Prioridad")
        self.tree.grid(row=0, column=0, columnspan=4, pady=5)

        # Entradas para agregar proceso
        ttk.Label(main_frame, text="Llegada:").grid(row=1, column=0)
        self.arrival_entry = ttk.Entry(main_frame, width=5)
        self.arrival_entry.grid(row=1, column=1)

        ttk.Label(main_frame, text="Rafaga:").grid(row=1, column=2)
        self.burst_entry = ttk.Entry(main_frame, width=5)
        self.burst_entry.grid(row=1, column=3)

        ttk.Label(main_frame, text="Prioridad:").grid(row=2, column=0)
        self.priority_entry = ttk.Entry(main_frame, width=5)
        self.priority_entry.grid(row=2, column=1)

        ttk.Button(main_frame, text="Agregar Proceso", command=self.add_process).grid(row=2, column=2, columnspan=2, pady=5)

        # Selector de algoritmo
        ttk.Label(main_frame, text="Algoritmo:").grid(row=3, column=0, pady=5)
        algo_combo = ttk.Combobox(
            main_frame,
            textvariable=self.selected_algorithm,
            values=["FCFS", "SJF", "Round Robin", "Prioridad"],
            state="readonly",
            width=15
        )
        algo_combo.grid(row=3, column=1)
        algo_combo.current(0)

        # Quantum
        ttk.Label(main_frame, text="Quantum:").grid(row=3, column=2)
        self.quantum_entry = ttk.Entry(main_frame, width=5, textvariable=self.quantum_value)
        self.quantum_entry.grid(row=3, column=3)

        # Botón de simulación
        ttk.Button(main_frame, text="Simular", command=self.run_simulation).grid(row=4, column=0, columnspan=4, pady=10)

        # Resultados
        self.result_text = tk.Text(main_frame, width=70, height=15)
        self.result_text.grid(row=5, column=0, columnspan=4, pady=5)

    def add_process(self):
        try:
            arrival = int(self.arrival_entry.get())
            burst = int(self.burst_entry.get())
            priority = int(self.priority_entry.get())

            pid = len(self.processes) + 1
            p = Process(pid, arrival, burst, priority)
            self.processes.append(p)

            self.tree.insert("", "end", values=(arrival, burst, priority))

            self.arrival_entry.delete(0, tk.END)
            self.burst_entry.delete(0, tk.END)
            self.priority_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

    def run_simulation(self):
        if not self.processes:
            messagebox.showwarning("Advertencia", "No hay procesos para simular.")
            return

        algo = self.selected_algorithm.get()
        quantum = self.quantum_value.get()

        # Copiar lista de procesos para evitar reutilización
        processes_copy = [Process(p.pid, p.arrival_time, p.burst_time, p.priority) for p in self.processes]

        if algo == "FCFS":
            result = fcfs(processes_copy)
        elif algo == "SJF":
            result = sjf(processes_copy)
        elif algo == "Round Robin":
            if not quantum.isdigit() or int(quantum) <= 0:
                messagebox.showerror("Error", "Quantum debe ser un número positivo.")
                return
            result = round_robin(processes_copy, int(quantum))
        elif algo == "Prioridad":
            result = priority_scheduling(processes_copy)
        else:
            messagebox.showerror("Error", "Algoritmo no válido.")
            return

        # Calcular métricas
        metrics = calculate_metrics(result)

        # Mostrar resultados
        self.result_text.delete("1.0", tk.END)

        self.result_text.insert(tk.END, "Resultados por proceso:\n")
        for m in metrics["per_process"]:
            line = (f"PID {m['pid']} | Inicio: {m['start_time']} | Fin: {m['completion_time']} | "
                    f"Turnaround: {m['turnaround_time']} | Espera: {m['waiting_time']} | "
                    f"Respuesta: {m['response_time']}\n")
            self.result_text.insert(tk.END, line)

        self.result_text.insert(tk.END, "\nPromedios:\n")
        avg = metrics["averages"]
        self.result_text.insert(tk.END, f"Turnaround promedio: {avg['average_turnaround_time']}\n")
        self.result_text.insert(tk.END, f"Espera promedio: {avg['average_waiting_time']}\n")
        self.result_text.insert(tk.END, f"Respuesta promedio: {avg['average_response_time']}\n")

