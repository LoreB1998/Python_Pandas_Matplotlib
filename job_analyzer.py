def calculate_salary(base_salary:float, bonus_rate = 0.1):
    """
    Calcola il salario, con bonus percentuale (0.0 - 1.0)

    Args:
        base_salary (float): Salario base
        bonus_rate (float, optional): Percentuale del bonus. Defaults to 0.1

    Returns:
        float: Salario totale
    """
    return base_salary * (1 + bonus_rate)

def calculate_bonus(total_salary:float, base_salary:float):
    """
    Calcola il bonus, dato il salario totale e il salario base

    Args:
        total_salary (float): Salario totale
        base_salary (float): Salario base
    Returns:
        float: Bonus in percentuale
    """
    return (total_salary - base_salary)/base_salary