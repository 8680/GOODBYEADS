import os

os.chdir('tmp')

def replace_content_in_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            if ':' not in line and '.js' not in line and '/' not in line:
                if line.strip().startswith("||") and line.strip().endswith("^"):
                    line = line.replace("||", "DOMAIN,").replace("^", ",reject")
                file.write(line)

def remove_whitelist_domains(input_file, whitelist_file):
    with open(whitelist_file, 'r') as whitelist:
        whitelist_domains = [entry.strip()[4:-1] for entry in whitelist if entry.strip().startswith('@@||') and entry.strip().endswith('^')]

    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(input_file, 'w') as file:
        for line in lines:
            if not any(domain in line for domain in whitelist_domains):
                file.write(line)

input_file_path = ".././data/rules/dns.txt"
output_file_path = ".././data/rules/qx.list"
whitelist_file_path = ".././data/mod/whitelist.txt"

replace_content_in_file(input_file_path, output_file_path)
remove_whitelist_domains(output_file_path, whitelist_file_path)
