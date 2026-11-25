"""The Funniest Sick-Day Excuse — makefun-sick-day-01."""

ENTRY = "Sorry, can't come in today — I threw my back out sneezing and the doctor said no lifting, no sitting, and definitely no spreadsheets."


def main():
    print(ENTRY)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
