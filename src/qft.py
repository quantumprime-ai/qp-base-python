from qiskit import QuantumCircuit, Aer, transpile
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector

# Crear un circuito cuántico con 3 qubits
qc = QuantumCircuit(3)

# Aplicar la QFT
qc.h(0)
qc.cp(1/2, 0, 1)
qc.h(1)
qc.cp(1/4, 0, 2)
qc.cp(1/2, 1, 2)
qc.h(2)

# Visualizar el circuito
print(qc)

# Simular el circuito
simulator = Aer.get_backend('aer_simulator')
qc_transpiled = transpile(qc, simulator)
result = simulator.run(qc_transpiled).result()
statevector = result.get_statevector()

# Visualizar el resultado
plot_histogram(result.get_counts(qc))
