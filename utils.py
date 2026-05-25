def is_valid_number():
    try:
        float(value)
        return True
    except ValueError:
        return False
