current = 4.2
temperature = 45
vibration = 1.2

print("INDUCTION MOTOR HEALTH MONITOR")
print("--------------------------------")
print(f"Current      : {current} A")
print(f"Temperature  : {temperature} °C")
print(f"Vibration    : {vibration} mm/s")

if current > 8:
    print("FAULT: OVER CURRENT")
elif temperature > 80:
    print("FAULT: OVER TEMPERATURE")
elif vibration > 5:
    print("FAULT: HIGH VIBRATION")
else:
    print("MOTOR STATUS: NORMAL")
