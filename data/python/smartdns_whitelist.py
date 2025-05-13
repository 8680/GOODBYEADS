import os
import re

# Change to the project root directory
os.chdir('tmp')

def convert_to_smartdns_whitelist(input_file, output_file):
    print("Generating SmartDNS whitelist rules...")
    
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
    
    domain_pattern = re.compile(r'@@\|\|([a-zA-Z0-9.-]+)\^')
    
    count = 0
    with open(output_file, 'w') as file:
        # Add header comment
        file.write("# SmartDNS whitelist rules for GOODBYEADS\n")
        file.write("# Homepage: https://github.com/8680/GOODBYEADS\n")
        file.write("# Format: address /domain/-\n\n")
        
        for line in lines:
            line = line.strip()
            # Look for AdBlock whitelist entries that use domain format (@@||domain^)
            match = domain_pattern.search(line)
            if match:
                domain = match.group(1)
                # Write SmartDNS whitelist rule format: address /domain/-
                file.write(f"address /{domain}/-\n")
                count += 1
    
    print(f"Generated {count} SmartDNS whitelist rules")

# Input from current allow.txt file
input_file_path = ".././data/rules/allow.txt"
# Output to new smartdns-whitelist.conf file
output_file_path = ".././data/rules/smartdns-whitelist.conf"

# Generate SmartDNS whitelist rules
convert_to_smartdns_whitelist(input_file_path, output_file_path) 