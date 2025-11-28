import nmap
import re
from colorama import Fore, Style
import nvdlib

def scan_cpe(ip):
    global candidate_os_cleaned
    global best_os_cleaned
    try:
        options = "-O -sV"
        nm = nmap.PortScanner()
        nm.scan(ip, arguments=options)
    except Exception as e:
        print(f"{Fore.RED}Scan failed: {e}{Style.RESET_ALL}")
        return None


    os_matches = []
    for host in nm.all_hosts():
        if 'osmatch' in nm[host]:
            os_matches = nm[host]['osmatch']
            break

    if not os_matches:
        print(f"{Fore.RED}No OS match data detected for {ip}.{Style.RESET_ALL}")
        return None

    print(f"\n{Fore.MAGENTA}Detected OS candidates for {ip}:{Style.RESET_ALL}")
    for match in os_matches:
        os_name = match.get('name', 'Unknown')
        accuracy = match.get('accuracy', '0')
        print(f"OS: {os_name} - Accuracy: {accuracy}%")

        best_match = max(os_matches, key=lambda x: int(x.get('accuracy', '0')))
        best_os = best_match.get('name', 'unkouwn').lower()
        best_accuracy = best_match.get('accuracy', '0')
        best_os_cleaned = re.sub(r"\s*-\s*\S*$", "", best_os)


        if not re.search(r'\d+', best_os_cleaned):

           sorted_os = sorted(os_matches, key=lambda x: int(x.get('accuracy', '0')), reverse=True)
           for candidate in sorted_os:
               candidate_os = candidate.get('name', 'unkouwn').lower()
               candidate_os_cleaned  = re.sub(r"\s*-\s*\S+$", "", candidate_os)

               if re.search(r'\d+', candidate_os_cleaned):
                  best_os_cleaned = candidate_os_cleaned
                  best_os = candidate_os
                  best_accuracy = candidate.get('accuracy', '0')
                  break
    print(f"\n{Fore.YELLOW}Cleaned OS Name: {best_os_cleaned}{Style.RESET_ALL}")
    print(f"\n{Fore.GREEN}Most likely OS: {best_os} with {best_accuracy}% accuracy{Style.RESET_ALL}")

    version_data = {}
    total_entries = 0
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            for port in sorted(nm[host][proto].keys()):
                port_info = nm[host][proto][port]
                state = port_info.get('state', 'unknown')
                product = port_info.get('product', '').strip()
                version = port_info.get('version', '').strip()
                print(f"Port: {port} | State: {state} | Product: {product} | Version: {version}")
                if product and version:
                    key = (product, version)
                    version_data[key] = version_data.get(key, 0) + 1
                    total_entries += 1

    if version_data:
        print(f"\n{Fore.CYAN}Service version distribution:{Style.RESET_ALL}")
        for key, count in version_data.items():
            percentage = (count / total_entries) * 100 if total_entries else 0
            print(f"Product: {key[0]}, Version: {key[1]} - {count} occurrences ({percentage:.2f}%)")
        best_port = max(version_data, key=lambda k: version_data[k])
        best_port_percentage = (version_data[best_port] / total_entries) * 100
        print(f"\n{Fore.GREEN}Most frequent service version: {best_port[0]} {best_port[1]} with {best_port_percentage:.2f}% occurrences{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}No service version info detected from ports.{Style.RESET_ALL}")

    try:
        cpe_results = nvdlib.searchCPE(keywordSearch=best_os_cleaned)
        if cpe_results:
            print(f"\n{Fore.CYAN}Available CPEs found:{Style.RESET_ALL}")
            for idx, cpe in enumerate(cpe_results, start=1):
                print(f"[{idx}] {cpe.cpeName}")
            print ("===============================================================")
            choice = int(input(f"{Fore.YELLOW}Select a CPE number from the list: {Style.RESET_ALL}"))
            if 1 <= choice <= len(cpe_results):
                selected_cpe = cpe_results[choice - 1].cpeName
                
                return selected_cpe
            else:
                print(f"{Fore.RED}Invalid selection. No CPE chosen.{Style.RESET_ALL}")
                return None
        else:
            print(f"{Fore.RED}No CPE candidate found for {best_os}{Style.RESET_ALL}")
            return None
    except Exception as e:
        print(f"{Fore.RED}Failed to retrieve CPE from nvdlib: {e}{Style.RESET_ALL}")
        return None

