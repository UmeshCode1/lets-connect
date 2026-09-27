"""Executive summary and KPI card generator."""
from __future__ import annotations
from typing import Union

def format_kpi_card(title: str, value: Union[str, int], subtitle: str = "") -> str:
    """Format single ASCII KPI metric card."""
    val_str = str(value)
    w = max(len(title), len(val_str), len(subtitle)) + 6
    border = "+" + "-" * w + "+"
    return f"{border}\n| {title:<{w-2}} |\n| {val_str:<{w-2}} |\n| {subtitle:<{w-2}} |\n{border}"
