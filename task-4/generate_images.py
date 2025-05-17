import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, LogFormatterMathtext, NullLocator

# Ensure output directory exists
os.makedirs('test_results', exist_ok=True)

# Load data
df30 = pd.read_csv('test_results/results_30.csv')
df70 = pd.read_csv('test_results/results_70.csv')

def plot_density(df, label):
    fig, ax = plt.subplots(figsize=(12, 6), dpi=100)
    
    ax.plot(df['n'], df['t_euler_ns'], color='purple', label='Euler (A)')
    ax.plot(df['n'], df['t_hamilton_avg_ns'], color='green',  label='Hamilton (B)')
    
    ax.set_xlim(100, 1500)
    ax.set_xticks(range(100, 1501, 100))
    ax.set_xlabel('n (liczba wierzchołków)')
    
    ax.set_yscale('log')
    ax.yaxis.set_major_locator(LogLocator(base=10))
    ax.yaxis.set_minor_locator(NullLocator())
    ax.yaxis.set_major_formatter(LogFormatterMathtext(base=10))
    ax.set_ylabel('Czas [ns]')
    
    ax.set_title(f'Porównanie algorytmów dla gęstości {label}%')
    ax.legend()
    
    ax.grid(which='major', axis='y', linestyle='-', linewidth=1, color='gray')
    ax.grid(False, axis='x')
    
    plt.tight_layout()
    out_path = f'test_results/plot_{label}.png'
    fig.savefig(out_path)
    plt.close(fig)
    print(f'Saved {out_path}')

plot_density(df30, '30')
plot_density(df70, '70')
