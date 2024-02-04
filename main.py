#This is an example of the file you must have in your main git branch
import perceval as pcvl
from perceval.converters import QiskitConverter
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi


    
    # Pre-requisites
qreg_q = QuantumRegister(3, 'q') # TO make 3 qubits
creg_c = ClassicalRegister(4, 'c') # TO make 4 classical bits
circuit = QuantumCircuit(qreg_q, creg_c) # TO make/compile the circuit
    
    
    # Code to make a CCZ gate using only 2 qubits at a time
circuit.h(qreg_q[2])
circuit.h(qreg_q[2])
circuit.cx(qreg_q[1], qreg_q[2])
circuit.tdg(qreg_q[2])
circuit.cx(qreg_q[0], qreg_q[2])
circuit.t(qreg_q[2])
circuit.cx(qreg_q[1], qreg_q[2])
circuit.tdg(qreg_q[2])
circuit.cx(qreg_q[0], qreg_q[2])
circuit.t(qreg_q[1])
circuit.t(qreg_q[2])
circuit.h(qreg_q[2])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.t(qreg_q[0])
circuit.tdg(qreg_q[1])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.h(qreg_q[2])
    
    
    # Portion to convert the circuit
qiskit_converter = QiskitConverter(pcvl.catalog, backend_name="Naive")
quantum_processor = qiskit_converter.convert(circuit, use_postselection=True)

    # Portion to print out the circuit must ignore/delete
    # pcvl.pdisplay(quantum_processor, recursive=False)
def get_CCZ() -> quantum_processor:
    return quantum_processor
    #return pcvl.catalog["postprocessed ccz"].build_processor()#.set_circuit(quantum_processor)
    