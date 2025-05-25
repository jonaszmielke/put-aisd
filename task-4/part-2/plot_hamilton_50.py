import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, LogFormatterSciNotation

# Determine base directory (script location or cwd)
try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    base_dir = os.getcwd()

# Paths
csv_path = os.path.join(base_dir, '../results', 'hamilton_50.csv')
out_png   = os.path.join(base_dir, '../results', 'plot_hamilton_50.png')

# Load data
df = pd.read_csv(csv_path)

# Create figure
fig, ax = plt.subplots(figsize=(12, 6), dpi=100)

# Plot average enumeration time
ax.plot(df['n'], df['avg_time_ns'],
        color='blue', linewidth=2, label='Avg enumeration time')

# X-axis: exact n values
ax.set_xticks(df['n'])
ax.set_xlim(df['n'].min(), df['n'].max())
ax.set_xlabel('n (number of vertices)')

# Y-axis: log scale + scientific notation
ax.set_yscale('log')
ax.yaxis.set_major_locator(LogLocator(base=10))
ax.yaxis.set_major_formatter(LogFormatterSciNotation(base=10, labelOnlyBase=False))
ax.set_ylabel('Average time [ns]')

# Title, legend, grid (only major horizontal lines)
ax.set_title('Hamiltonian cycle enumeration time (50% density)')
ax.legend()
ax.grid(which='major', axis='y', linestyle='-', linewidth=1, color='gray')
ax.grid(False, axis='x')

plt.tight_layout()
os.makedirs(os.path.dirname(out_png), exist_ok=True)
fig.savefig(out_png)
plt.show()

print(f"Plot saved to {out_png}")
