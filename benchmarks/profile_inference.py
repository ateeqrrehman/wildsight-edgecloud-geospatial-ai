import statistics
import time
from typing import Any, Callable, Iterable


def _percentile(values: list[float], percentile: int) -> float | None:
    if not values:
        return None

    sorted_values = sorted(values)
    index = int((percentile / 100) * (len(sorted_values) - 1))
    return sorted_values[index]


def profile_function(
    inference_fn: Callable[[Any], Any],
    inputs: Iterable[Any],
    warmup_runs: int = 3,
) -> dict[str, float | int | None]:
    """
    Profile an inference function over a collection of inputs.

    Args:
        inference_fn: Callable inference function.
        inputs: Iterable of input samples.
        warmup_runs: Number of warmup calls before measurement.

    Returns:
        Dictionary containing latency, throughput, and runtime metrics.
    """
    input_items = list(inputs)

    for item in input_items[:warmup_runs]:
        inference_fn(item)

    latencies_ms: list[float] = []
    total_start = time.perf_counter()

    for item in input_items:
        start = time.perf_counter()
        inference_fn(item)
        end = time.perf_counter()
        latencies_ms.append((end - start) * 1000)

    total_end = time.perf_counter()
    total_runtime_sec = total_end - total_start

    throughput = (
        len(input_items) / total_runtime_sec
        if total_runtime_sec > 0
        else 0
    )

    return {
        "count": len(input_items),
        "avg_latency_ms": statistics.mean(latencies_ms) if latencies_ms else None,
        "p50_latency_ms": _percentile(latencies_ms, 50),
        "p95_latency_ms": _percentile(latencies_ms, 95),
        "p99_latency_ms": _percentile(latencies_ms, 99),
        "throughput_items_per_sec": throughput,
        "total_runtime_sec": total_runtime_sec,
    }


if __name__ == "__main__":
    print(
        "This module provides reusable profiling utilities. "
        "Import profile_function into an inference script to benchmark model calls."
    )