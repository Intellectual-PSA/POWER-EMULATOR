import psutil
import time

# Define the sampling interval in seconds
interval = 1

# Define the path and name of the output file
output_file = 'power_usage.txt'

# Open the output file for writing
with open(output_file, 'w') as f:
    # Write the header row to the output file
    f.write('Timestamp, Voltage (V), Amperage (A), Wattage (W)\n')
    
    # Start an infinite loop to sample power usage data
    while True:
        # Get the current timestamp
        timestamp = time.time()
        
        # Get the current voltage, amperage, and wattage values
        voltage = psutil.sensors_battery().voltage
        amperage = psutil.sensors_battery().current
        wattage = voltage * amperage
        
        # Write the data to the output file
        f.write('{0},{1},{2},{3}\n'.format(timestamp, voltage, amperage, wattage))
        
        # Wait for the sampling interval
        time.sleep(interval)
