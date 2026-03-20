import argparse
from pathlib import Path
import pandas as pd


def load_airbnb_csv(path: str | None = None) -> pd.DataFrame:
    """Load the Airbnb CSV into a pandas DataFrame.

    If `path` is None the function will look for `airbnb_price.csv` next to this script.
    """
    default_path = Path(__file__).parent / "airbnb_price.csv"
    p = Path(path) if path else default_path
    if not p.exists():
        raise FileNotFoundError(f"CSV file not found: {p}")

    df = pd.read_csv(p)

    # Try to convert obvious date-like columns (e.g., "last_review") to datetimes.
    for col in df.columns:
        lc = col.lower()
        if "date" in lc or "review" in lc or "time" in lc:
            try:
                parsed = pd.to_datetime(df[col], errors="coerce")
                if parsed.notna().sum() > 0:
                    df[col] = parsed
            except Exception:
                pass

    return df


def main() -> None:
    parser = argparse.ArgumentParser(description="Load Airbnb CSV into a pandas DataFrame and show summary")
    parser.add_argument("csv", nargs="?", help="Path to the CSV file (optional)")
    args = parser.parse_args()

    df = load_airbnb_csv(args.csv)

    print("DataFrame shape:", df.shape)
    print("\nInfo:")
    print(df.info())
    print("\nFirst 5 rows:")
    print(df.head().to_string(index=False))


if __name__ == "__main__":
    main()
