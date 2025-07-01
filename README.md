# Simulador de Algoritmos de Planificación de CPU

Proyecto elaborado por: 

**Isabella Noy**  

**Juan González**

**Kevin Monasterios**

**Mauricio Correa**

Materia **Sistemas Operativos**  
Universidad Católica Andrés Bello

---

## Descripción

Este simulador implementa y compara los principales algoritmos de planificación de CPU:

- **FCFS** (First Come, First Served)
- **SJF** (Shortest Job First, no apropiativo)
- **Round Robin** (quantum configurable)
- **Prioridades** (no apropiativo)

Permite:

-Crear procesos manualmente  
-Configurar parámetros de simulación  
-Calcular métricas de rendimiento (Turnaround, Waiting, Response Time)  
-Mostrar resultados en tabla  

---

## Requisitos

- Python 3.10+
- Tkinter (incluido con Python)
- matplotlib
- pandas

---

## Instalación y ejecución

### 1. Clonar o copiar el proyecto

```git clone https://github.com/isabellanoy/Operativos-Project.git```

Navega a tu carpeta de trabajo:

```cd ~/Documents```

Si ya tienes la carpeta creada, entra en ella:

```cd cpu_scheduler_simulator```

## 2. Crear entorno virtual


```python3 -m venv venv```

## 3. Activar el entorno virtual

En Linux/macOS:

```source venv/bin/activate```

En Windows (PowerShell):

```venv\Scripts\Activate.ps1```

## 4. Instalar dependencias


```pip install matplotlib pandas```

## 5. Ejecutar el simulador


```python main.py```

# Casos de prueba sugeridos

A continuación puedes ingresar manualmente estos procesos en la interfaz para probar cada algoritmo:

```
Conjunto 1 (Básico)
Proceso	Llegada	Ráfaga	Prioridad
P1	0	8	3
P2	1	4	1
P3	2	9	4
P4	3	5	2

Conjunto 2 (Procesos variados)
Proceso	Llegada	Ráfaga	Prioridad
P1	0	10	2
P2	2	3	1
P3	4	6	3
P4	6	1	1
P5	8	4	2

Round Robin
Para este conjunto se recomienda un quantum de 2 o 4.
```

# Cómo usar

## Agregar procesos:

1. Completa los campos Llegada, Ráfaga y Prioridad.
2. Haz clic en Agregar Proceso.
3. Repite para todos los procesos.

## Elegir algoritmo:

1. Usa el desplegable Algoritmo.
2. Si usas Round Robin, indica el quantum.

## Simular:

1. Haz clic en Simular.
2. Observa los resultados en el panel inferior.
