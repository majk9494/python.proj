# 2 Öva på TDD
# equivalence class (9/5) C + 32

def celsius_to_fahrenheit(degree):
    if degree < -273.15:
        return None
    return degree * 1.8 + 32
