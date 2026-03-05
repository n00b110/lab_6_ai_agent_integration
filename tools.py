import pandas as pd

df = pd.read_csv("Toyota_Stock_Prices_1980_2026.csv")

df["Date"] = pd.to_datetime(df["Date"])


def latest_price() -> float:
    """
    Returns the most recent closing price.
    """
    latest = df.sort_values("Date").iloc[-1]
    return float(latest["Close"])


def average_price_year(year: int) -> float:
    """
    Calculate average closing price for a given year.
    """
    year_data = df[df["Date"].dt.year == year]

    if year_data.empty:
        return None

    return float(year_data["Close"].mean())


def highest_price() -> float:
    """
    Return highest recorded closing price.
    """
    return float(df["Close"].max())


def price_on_date(date: str):
    """
    Return closing price for a specific date.
    Date format: YYYY-MM-DD
    """

    result = df[df["Date"] == date]

    if result.empty:
        return None

    return float(result.iloc[0]["Close"])


def average_volume() -> float:
    """
    Return average trading volume.
    """
    return float(df["Volume"].mean())


import pandas as pd

df = pd.read_csv("Toyota_Stock_Prices_1980_2026.csv")
df["Date"] = pd.to_datetime(df["Date"])


def latest_price() -> float:
    latest = df.sort_values("Date").iloc[-1]
    return float(latest["Close"])


def average_price_year(year: int) -> float:
    year_data = df[df["Date"].dt.year == year]
    return float(year_data["Close"].mean())


def highest_price() -> float:
    return float(df["Close"].max())


def price_on_date(date: str):
    result = df[df["Date"] == date]
    if result.empty:
        return None
    return float(result.iloc[0]["Close"])


def average_volume() -> float:
    return float(df["Volume"].mean())
