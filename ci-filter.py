import glob
import os


def filter(filepath: str) -> str:
    with open(filepath, encoding="utf-8") as f:
        lines = f.readlines()

    result = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("| Tz") or stripped.startswith("|----"):
            result.append(line)
        elif "✓" in line:
            result.append(line)

    if len(result) > 2:
        return "".join(result)
    return ""


def main():
    for filepath in sorted(glob.glob("full/*.md")):
        filtered = filter(filepath)
        outpath = os.path.basename(filepath)
        if filtered:
            with open(outpath, "w", encoding="utf-8") as f:
                f.write(filtered)
            print(f"Written: {outpath}")
        else:
            if os.path.exists(outpath):
                os.remove(outpath)
                print(f"Removed (no ticks): {outpath}")
            else:
                print(f"Skipped (no ticks): {filepath}")


if __name__ == "__main__":
    main()
