from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute, Aer
import numpy as np

qc = QuantumCircuit()

q = QuantumRegister(58, 'q')
c = ClassicalRegister(57, 'c')

qc.add_register(q)
qc.add_register(c)

def peres1(a, b, c, d, e, f):
  qc.cx(a, d)
  qc.cx(b, e)
  qc.cx(a, e)
  qc.ccx(a, b, f)
  qc.cx(c, f)

def peresfulladder(a, b, c, d, e, f, g, h, i, j):
  qc.cx(a, d)
  qc.cx(b, e)
  qc.cx(a, e)
  qc.ccx(a, b, f)
  qc.cx(c, f)
  qc.cx(e, h)
  qc.cx(f, i)
  qc.cx(e, i)
  qc.ccx(e, f, j)
  qc.cx(g, j)

qc.x(q[0])
qc.x(q[17])
qc.x(q[45])
peres1(q[0], q[1], q[2], q[3], q[4], q[5])
peresfulladder(q[7], q[8], q[9], q[10], q[11], q[12], q[13], q[14], q[15], q[16])
peres1(q[17], q[15], q[18], q[19], q[20], q[21])
peresfulladder(q[5], q[21], q[22], q[23], q[24], q[25], q[26], q[27], q[28], q[29])
peres1(q[30], q[31], q[32], q[33], q[34], q[35])
qc.measure(q[21], c[21])
qc.measure(q[5], c[5])
peresfulladder(q[36], q[35], q[37], q[38], q[39], q[40], q[41], q[42], q[43], q[44])
peres1(q[45], q[43], q[46], q[47], q[48], q[49])
qc.measure(q[49], c[45])
peresfulladder(q[28], q[49], q[50], q[51], q[52], q[53], q[54], q[55], q[56], q[57])
qc.measure(q[56], c[56])

backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend=backend)
job_result = job.result()
print(job_result.get_counts(qc))
