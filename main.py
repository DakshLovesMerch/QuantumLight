import perceval as pcvl
from perceval.converters import QiskitConverter
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi
from enum import Enum
import math
import auto_grader

p=pcvl.catalog['postprocessed ccz'].build_processor()
pcvl.pdisplay(p, recursive=True)
states={pcvl.BasicState('|1,0,1,0,1,0>'): '000',
               pcvl.BasicState('|1,0,1,0,0,1>'): '001',
               pcvl.BasicState('|1,0,0,1,1,0>'): '010',
               pcvl.BasicState('|1,0,0,1,0,1>'): '011',
               pcvl.BasicState('|0,1,1,0,1,0>'): '100',
               pcvl.BasicState('|0,1,1,0,0,1>'): '101',
               pcvl.BasicState('|0,1,0,1,1,0>'): '110',
               pcvl.BasicState('|0,1,0,1,0,1>'): '111'}
target = {"000": "000", "001": "001", "010": "010", "011": "011",
              "100": "100", "101": "101", "110": "111", "111": "110"}
ca = pcvl.algorithm.Analyzer(pcvl.catalog["postprocessed ccz"].build_processor(), states)
ca.compute(target)
########################################################################################################################3

qreg_q = QuantumRegister(3, 'q')
creg_c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)
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
qiskit_converter = QiskitConverter(pcvl.catalog, backend_name="Naive")
quantum_processor = qiskit_converter.convert(circuit, use_postselection=True)

def get_CCZ() -> pcvl.Processor:
    return quantum_processor
