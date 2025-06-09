import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def save_results(
    results_dict: dict,
    x_label: str,
    x_key: str,
    scenario_name: str,
) -> None:
    """
    Saves experiment results to CSV and creates one figure with two subplots:
    - Top: execution time vs x (line chart)
    - Bottom: relative error vs x (bar chart in red)
    X axis ticks at 100, 200, …, 1000; error axis in percent with one decimal.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, 'results')
    os.makedirs(output_dir, exist_ok=True)

    # Flatten results into a DataFrame
    records = []
    for method in ("greedy", "dynamic"):
        for x, metrics in results_dict[method].items():
            records.append({
                "method": method,
                x_key: x,
                "value": metrics["value"],
                "time_seconds": metrics["time"]
            })
    df = pd.DataFrame(records)

    # Save CSV
    csv_path = os.path.join(output_dir, f"{scenario_name}.csv")
    df.to_csv(csv_path, index=False)
    print(f"Saved results CSV: results/{scenario_name}.csv")

    # Pivot for time and compute error
    time_pivot = df.pivot(index=x_key, columns="method", values="time_seconds")
    value_pivot = df.pivot(index=x_key, columns="method", values="value")
    rel_error = ((value_pivot["dynamic"] - value_pivot["greedy"]) /
                  value_pivot["dynamic"]).reset_index()
    rel_error.columns = [x_key, "relative_error"]

    # X-axis ticks at 100,200,...,1000
    xticks = list(range(100, 2001, 100))

    # Create combined figure
    fig, (ax_time, ax_error) = plt.subplots(2, 1, sharex=True, figsize=(16, 10))

    # Top: execution time (line chart)
    for method in time_pivot.columns:
        ax_time.plot(
            time_pivot.index,
            time_pivot[method],
            marker='o',
            label=method.title()
        )
    ax_time.set_ylabel("Execution Time (s)")
    ax_time.set_title(f"Execution Time vs {x_label}")
    ax_time.legend()
    ax_time.set_xticks(xticks)

    # Bottom: relative error (bar chart)
    ax_error.bar(
        rel_error[x_key],
        rel_error["relative_error"],
        width=80,
        color='red',
        label="Greedy Relative Error"
    )
    ax_error.set_xlabel(x_label)
    ax_error.set_ylabel("Relative Error (%)")
    ax_error.set_title("Relative Error of Greedy")
    ax_error.legend()
    ax_error.set_xticks(xticks)
    ax_error.yaxis.set_major_formatter(
        mtick.PercentFormatter(xmax=1.0, decimals=1)
    )

    plt.tight_layout()
    combined_path = os.path.join(output_dir, f"{scenario_name}.png")
    fig.savefig(combined_path)
    plt.close(fig)
    print(f"Saved plot: results/{scenario_name}.png")