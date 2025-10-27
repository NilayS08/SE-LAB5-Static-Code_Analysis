"""Simple in-memory inventory system with JSON persistence."""

import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add quantity for an item and append an audit log entry."""
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Reduce quantity for an item; delete if quantity becomes non-positive."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        # Ignore if item does not exist
        pass
    except TypeError:
        # Ignore invalid arithmetic (e.g., wrong types)
        pass


def get_qty(item):
    """Return current quantity of an item; may raise KeyError if missing."""
    return stock_data[item]


def load_data(file_path="inventory.json"):
    """Load inventory from a JSON file into stock_data."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            stock_data.clear()
            stock_data.update(data)
    except FileNotFoundError:
        # If file missing, keep current in-memory data
        pass
    except json.JSONDecodeError:
        # If file is corrupted, keep current in-memory data
        pass


def save_data(file_path="inventory.json"):
    """Persist current stock_data to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)


def print_data():
    """Print a simple inventory report."""
    print("Items Report")
    for key, val in stock_data.items():
        print(key, "->", val)


def check_low_items(threshold=5):
    """Return list of item names with quantity below threshold."""
    result = []
    for key, val in stock_data.items():
        if val < threshold:
            result.append(key)
    return result


def main():
    """Demonstrate basic inventory operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item("widget", 5)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
