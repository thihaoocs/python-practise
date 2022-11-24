import class_decorator_tank as tank

myTank = tank.Original_tank()
print("Upgraded Part: {0}, Damage {1}, Strength {2}".format(myTank.get_upgraded_part(),myTank.get_damage(),myTank.get_strength()))

# myTank = tank.ERA(myTank)
upgradedTank = tank.Main_Battery(myTank)
print("Upgraded Part: {0}, Damage {1}, Strength {2}".format(upgradedTank.get_upgraded_part(),upgradedTank.get_damage(),upgradedTank.get_strength()))