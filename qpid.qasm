OPENQASM 2.0;
include "qelib1.inc";
qreg q[58];
creg c[57];
gate peres1 a, b, c, d, e, f
{
  cx a, d;
  cx b, e;
  cx a, e;
  ccx a, b, f;
  cx c, f;
}

gate peresfulladder a, b, c, d, e, f, g, h, i, j
{
  cx a, d;
  cx b, e;
  cx a, e;
  ccx a, b, f;
  cx c, f;
  cx e, h;
  cx f, i;
  cx e, i;
  ccx e, f, j;
  cx g, j;
}

x q[0];
x q[17];
x q[45];
peres1 q[0], q[1], q[2], q[3], q[4], q[5];
peresfulladder q[7], q[8], q[9], q[10], q[11], q[12], q[13], q[14], q[15], q[16];
peres1 q[17], q[15], q[18], q[19], q[20], q[21];
peresfulladder q[5], q[21], q[22], q[23], q[24], q[25], q[26], q[27], q[28], q[29];
peres1 q[30], q[31], q[32], q[33], q[34], q[35];
measure q[21] -> c[21];
measure q[5] -> c[5];
peresfulladder q[36], q[35], q[37], q[38], q[39], q[40], q[41], q[42], q[43], q[44];
peres1 q[45], q[43], q[46], q[47], q[48], q[49];
measure q[49] -> c[45];
peresfulladder q[28], q[49], q[50], q[51], q[52], q[53], q[54], q[55], q[56], q[57];
measure q[56] -> c[56];
