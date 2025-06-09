import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def save_results(
    results_dict: dict,
    x_label: str,
    x_key: str,
    scenario_name: str,
    number_of_items_constant: int = None,
    capacity_constant: int = None,
) -> None:
    """
    Saves experimental results to CSV and produces a combined plot
    with two subplots: execution time and relative error.
    The error line is red, the x-axis uses ticks at 100, 200, …, 1000,
    and the relative-error y-axis is shown in percent with one decimal place.
    """
    output_directory = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'results'
    )
    os.makedirs(output_directory, exist_ok=True)

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

    # Compute relative error series
    df_pivot = df.pivot(index=x_key, columns="method", values="value")
    rel_error_series = (
        df_pivot["dynamic"] - df_pivot["greedy"]
    ) / df_pivot["dynamic"]
    df_error = rel_error_series.reset_index().rename(
        columns={0: "relative_error"}
    )

    # Save CSV
    csv_filename = f"{scenario_name}.csv"
    csv_path = os.path.join(output_directory, csv_filename)
    df.to_csv(csv_path, index=False)
    print(f"Saved results CSV: results/{csv_filename}")

    # Fixed x-axis ticks at 200, 400, …, 2000
    xticks = list(range(200, 2001, 200))

    # Create combined figure with 2 subplots
    fig, (ax_time, ax_error) = plt.subplots(
        2, 1, sharex=True, figsize=(12, 8)
    )

    # Plot execution time on first subplot
    for method, group in df.groupby("method"):
        ax_time.plot(
            group[x_key],
            group["time_seconds"],
            marker='o',
            label=method.title()
        )
    ax_time.set_ylabel("Execution Time (s)")
    ax_time.set_title(f"Execution Time vs {x_label}")
    ax_time.legend()
    ax_time.set_xticks(xticks)

    # Plot relative error on second subplot (red line)
    ax_error.plot(
        df_error[x_key],
        df_error["relative_error"],
        color='red',
        marker='o',
        label="Greedy Relative Error"
    )
    ax_error.set_xlabel(x_label)
    ax_error.set_ylabel("Relative Error (%)")
    ax_error.set_title("Relative Error of Greedy")
    ax_error.legend()
    ax_error.set_xticks(xticks)

    # Format y-axis as percentage with one decimal place
    ax_error.yaxis.set_major_formatter(mtick.PercentFormatter(
        xmax=1.0,
        decimals=1
    ))

    plt.tight_layout()

    # Save combined plot
    combined_filename = f"{scenario_name}.png"
    combined_path = os.path.join(output_directory, combined_filename)
    fig.savefig(combined_path)
    plt.close(fig)
    print(f"Saved plot: results/{scenario_name}.png")
