import perceval as pcvl
from perceval.components import catalog
from perceval.converters import QiskitConverter, MyQLMConverter
from perceval.algorithm import Analyzer, Sampler

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qiskit_circuit = QuantumCircuit(3)

qiskit_circuit.h(0)

qiskit_circuit.cx(0, 1)
qiskit_circuit.cx(0, 2)
qiskit_circuit.draw()

state = Statevector.from_int(0, 2**3)

state = state.evolve(qiskit_circuit)

state.draw('latex')
qiskit_converter = QiskitConverter(catalog, backend_name="Naive")
quantum_processor = qiskit_converter.convert(qiskit_circuit, use_postselection=True)
pcvl.pdisplay(quantum_processor, recursive=True)
quantum_processor.with_input(pcvl.LogicalState([0,0,0]))

sampler = Sampler(quantum_processor)

output_distribution = sampler.probs()["results"]
pcvl.pdisplay(output_distribution, precision=1e-2, max_v = 4)
u = quantum_processor.linear_circuit().compute_unitary(use_symbolic=False)
ub = (pcvl.Circuit(2)
      // pcvl.BS(theta=pcvl.Parameter("theta"))
      // (0, pcvl.PS(phi=pcvl.Parameter("φ_a"))))

pc_norm = pcvl.Circuit.decomposition(u, ub, shape="triangle")
pcvl.pdisplay(pc_norm, compact=True, render_size=0.5)
