import perceval as pcvl
import auto_grader
import math
pcvl.catalog["postprocessed ccz"].build_processor
def get_CCZ() -> pcvl.Processor:
    return pcvl.catalog["postprocessed_ccz"].build_processor()
auto_grader.n_photons=1203103123012931
auto_grader.n_modes=10221525125


states={pcvl.BasicState('|1,0,1,0,1,0>'): '000',
        pcvl.BasicState('|1,0,1,0,0,1>'): '001',
        pcvl.BasicState('|1,0,0,1,1,0>'): '010',
        pcvl.BasicState('|1,0,0,1,0,1>'): '011',
        pcvl.BasicState('|0,1,1,0,1,0>'): '100',
        pcvl.BasicState('|0,1,1,0,0,1>'): '101',
        pcvl.BasicState('|0,1,0,1,1,0>'): '110',
        pcvl.BasicState('|0,1,0,1,0,1>'): '111'}


target={"000": "000", "001": "001", "010": "010", "011": "011",
              "100": "100", "101": "101", "110": "111", "111": "110"}


ca = pcvl.algorithm.Analyzer(pcvl.catalog["postprocessed ccz"].build_processor(), states)

ca.compute(target)

print(ca.performance)

print(ca.fidelity)