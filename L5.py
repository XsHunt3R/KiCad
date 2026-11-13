import pandas as pd
import matplotlib.pyplot as plt

discrete = pd.read_csv("L4.csv")
s7 = pd.read_csv("S7.csv")

plt.plot(discrete['VIN']/4.94E+00, discrete['V(vout)']/4.94E+00,
         label='Discrete CMOS Inverter')

plt.plot(s7['Vin']/1.099972, s7['V(out)']/1.099972,
         label='S7 CMOS Inverter')

plt.xlabel('Input Voltage (V)')
plt.ylabel('Output Voltage (V)')
plt.title('Voltage Transfer Characteristics')

plt.grid(True)
plt.legend()
plt.savefig('L5_plot.png', dpi=300)
plt.show()