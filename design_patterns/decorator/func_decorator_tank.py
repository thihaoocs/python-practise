def upgrade_gun(original_tank):
    def wrapper(*args, **kwargs):
        damage = 135
        strength = 100
        print('Gun upgraded....')
        return original_tank(damage, strength)
    return wrapper

def upgrade_armor(original_tank):
    def wrapper(*args, **kwargs):
        damage = 100
        strength = 120
        print('Armor upgraded.....')
        return original_tank(damage, strength)
    return wrapper

@upgrade_armor
@upgrade_gun
def show_tank_status(damage, strength):
    print(f"Upgraded Part: Gun, Damage {damage}, Strength {strength}")

show_tank_status(100,100)