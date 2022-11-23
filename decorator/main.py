import tank

myTank = tank.Original_tank()

# myTank = tank.ERA(myTank)
myTank = tank.Main_Battery(myTank)
print("Upgraded Part: {0}, Damage {1}, Strength {2}".format(myTank.get_upgraded_part(),myTank.get_damage(),myTank.get_strength()))