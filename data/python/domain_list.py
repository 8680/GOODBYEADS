import os

# Change to the project root directory
os.chdir('tmp')

def extract_domains(input_file, output_file):
    print("Extracting domain list...")
    
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
    
    count = 0
    with open(output_file, 'w') as file:
        # Add header comment
        file.write("# GOODBYEADS Domain List\n")
        file.write("# Homepage: https://github.com/8680/GOODBYEADS\n")
        file.write("# Generated from GOODBYEADS DNS rules\n\n")
        
        for line in lines:
            line = line.strip()
            # Check if the line starts with "||" and ends with "^" (adblock DNS syntax)
            if line.startswith("||") and line.endswith("^"):
                # Extract domain from the rule (remove || prefix and ^ suffix)
                domain = line[2:-1]
                # Write only the domain name without any prefix or suffix
                file.write(f"{domain}\n")
                count += 1
    
    print(f"Extracted {count} domains to domain list")

# Input from current dns.txt file
input_file_path = ".././data/rules/dns.txt"
# Output to new ad-domain.txt file
output_file_path = ".././data/rules/ad-domain.txt"

# Generate domain list
extract_domains(input_file_path, output_file_path) 