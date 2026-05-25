def is_valid_numder():
    try:
        float(value)
        return True
    except ValueError:
        return False
