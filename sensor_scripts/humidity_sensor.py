# humidity_sensor.py
import subprocess
import re

# program_output = os.system("./loldht 7")
program_output = subprocess.check_output(["./loldht", "7"])
humidity_pattern = 'Humidity = ([^\ ]*)'
temperature_pattern = 'Temperature = ([^\ ]*)'
humidity = re.search(humidity_pattern, program_output).group(1)
temperature = re.search(temperature_pattern, program_output).group(1)

print("Humidity " + str(humidity))
print("Temperature " + str(temperature))