import json

def csv_to_records(text: str) -> list[dict]:
    if not text.strip():
        return []

    lines = text.strip().splitlines()

    headers = [item.strip() for item in lines[0].split(",")]

    records = []

    for line in lines[1:]:
        if not line.strip():
            continue

        values = [item.strip() for item in line.split(",")]

        record = dict(zip(headers, values))
        records.append(record)

    return records


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list = None

    for line in lines:
        line = line.split("#", 1)[0].strip()

        if not line:
            continue
        
        if line.startswith("-"):
            if current_list is not None:
                value = line[1:].strip()
                result[current_list].append(value)
            continue
        
        if ":" not in line:
            continue
        
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        
        if not value:
            result[key] = []
            current_list = key
            continue

        current_list = None

        if value.lower() in ("true", "yes"):
            value = True
        elif value.lower() in ("false", "no"):
            value = False
        else:
            try:
                if "," in value:
                    value = float(value.replace(",", "."))
                elif "." in value:
                    value = float(value)
                else:
                    value = int(value)
            except ValueError:
                pass

        result[key] = value

    return result


def merge_by_key(
    rows: list[dict],
    extra: dict,
    key: str = "id"
) -> list[dict]:
    result = []

    for row in rows:
        record = {}

        additional = extra.get(row.get(key), {})

        record.update(additional)

        record.update(row)

        result.append(record)

    return result


def records_to_json(records: list[dict]) -> str:
    return json.dumps(
        records,
        ensure_ascii=False,
        indent=2,
        sort_keys=True
    )
