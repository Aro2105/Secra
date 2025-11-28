import nvdlib
import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry



def search_cve(cpe_name):
    try:
        
        cves = nvdlib.searchCVE(cpeName=cpe_name) #timeout=10)
        vulnrabilitice = []
        
        for vuln in cves:
            cve_id = vuln.id
            description = vuln.descriptions[0].value
            severity = getattr(vuln, 'v31severity', None) or \
                       getattr(vuln, 'v30severity', None) or \
                       getattr(vuln, 'v2severity', "None ") or \
                       getattr(vuln, 'baseScore', "0")
            metrics = vuln.metrics
            cvss_score4 = None
            cvss_score3 = None
            cvss_score31 = None
            cvss_score2 = None

            if 'cvssMetricV40' in metrics:
                cvss_score4 = vuln.v40score
            if 'cvssMetricV30' in metrics:
                cvss_score3 = vuln.v30score
            if 'cvssMetricV31' in metrics:
                cvss_score31 = vuln.v31score
            if 'cvssMetricV2' in metrics:
                cvss_score2 = vuln.v2score

            vulnrabilitice.append({'v2score': cvss_score2})
            vulnrabilitice.sort(key=lambda x: x['v2score'] if x['v2score'] is not None else 0)

            print(f"\nCVE ID: {cve_id}")
            print(f"Descriptions: {description}")
            print(f"Severity: {severity}")
            print(f"CVSS_ScoreV40: {cvss_score4}")
            print(f"CVSS_ScoreV31: {cvss_score31}")
            print(f"CVSS_ScoreV30: {cvss_score3}")
            print("===============================================================")
            
    except Exception as e:
        print(f"Error Give vulnrability {e}")
        return