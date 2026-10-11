def celsius_converter(f_temp):
    return round((float(f_temp) - 32) * 5 / 9, 2)


def parse_and_clean(line):
    parts = [p.strip() for p in line.split("|")]
    if len(parts) != 5 or not all(parts) or parts[4] != "ACTIVE":
        return None
    try:
        float(parts[2]) 
    except ValueError:
        return None
    return parts


skipped = 0
with open("environmental_raw.txt") as infile, open("environmental_clean.csv", "w") as outfile:
    outfile.write("Timestamp,StationID,Temp(C),Humidity(%)\n")
    next(infile)  # skip header row
    for line in infile:
        row = parse_and_clean(line)
        if row is None:
            skipped += 1
            continue
        row[2] = celsius_converter(row[2])
        outfile.write(",".join(map(str, row[:4])) + "\n")

print(f"Corrupted lines skipped: {skipped}")
