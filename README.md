# QuantumLight

The goal of this challenge is to better understand the link between the linear optical circuit as a unitary on the modes and the resulting unitary operator on the Fock space and how we can design the search of more complex linear optical gates.

Our code sets up a quantum processor, defines quantum states and a target mapping, performs computation using an analyzer, and then prints the performance and fidelity results of the computation. In the CCZ gate, there are 3 qubits configured with 6 main modes and 6 herald modes. 
We created a get_CCZ() function which included the following: 
- Built a processor using the 'build_processor' function and the 'postprocessed ccz' out of the pcvl catalog. 
- Displayed the gate using the 'pdisplay' function and the parameter 'recursive = True' which makes the gate more detailed.
- Created states, which are the dictionary in which each is a quantum state. We created them using the 'pcvl.BasicState' function 
- Truth table which is used to compare our values to the theoretically perfect values. 
- Used the Anaylser which helps evaluate the performance of quantum algorithms or circuits.
- Printed the performance and fidelity of the CCZ gate.

This function creates the CCZ gate and returns a perceval Processor.
Fidelity is the distance between your gate and the theoretical perfect one and performance is the ratio of how many measurement we keep and how many measurement we throw away.


