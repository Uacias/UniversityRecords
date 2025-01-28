def validate_pesel(pesel: str) -> bool:
    if len(pesel) != 11 or not pesel.isdigit():
        return False

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    checksum = sum(int(pesel[i]) * weights[i] for i in range(10))
    control_digit = (10 - (checksum % 10)) % 10

    return control_digit == int(pesel[10])


def decode_pesel(pesel: str):
    if not validate_pesel(pesel):
        return None

    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    if 1 <= month <= 12:
        year += 1900
    elif 21 <= month <= 32:
        month -= 20
        year += 2000
    elif 41 <= month <= 52:
        month -= 40
        year += 2100
    elif 61 <= month <= 72:
        month -= 60
        year += 2200
    elif 81 <= month <= 92:
        month -= 80
        year += 1800
    else:
        return None

    gender_digit = int(pesel[9])
    gender = "Mężczyzna" if gender_digit % 2 != 0 else "Kobieta"

    return {"data_urodzenia": f"{year:04d}-{month:02d}-{day:02d}", "płeć": gender}
