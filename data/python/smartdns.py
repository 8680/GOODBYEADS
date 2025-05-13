import os

# Change to the project root directory
os.chdir('tmp')

def convert_to_smartdns_format(input_file, output_file):
    print("Generating SmartDNS rules...")
    
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    count = 0
    with open(output_file, 'w') as file:
        # Add header comment
        file.write("# SmartDNS rules for GOODBYEADS\n")
        file.write("# Homepage: https://github.com/8680/GOODBYEADS\n")
        file.write("# Format: address /domain/#\n\n")
        
        for line in lines:
            line = line.strip()
            # Check if the line starts with "||" and ends with "^" (adblock DNS syntax)
            if line.startswith("||") and line.endswith("^"):
                # Extract domain from the rule (remove || prefix and ^ suffix)
                domain = line[2:-1]
                # Write SmartDNS rule format: address /domain/#
                file.write(f"address /{domain}/#\n")
                count += 1
    
    print(f"Generated {count} SmartDNS rules")

# Input from current dns.txt file
input_file_path = ".././data/rules/dns.txt"
# Output to new smartdns.conf file
output_file_path = ".././data/rules/smartdns.conf"

# Generate SmartDNS rules
convert_to_smartdns_format(input_file_path, output_file_path) 