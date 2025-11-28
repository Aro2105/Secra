import nvdlib
import time
def search_cpe(os_name, version):
    search_query = f"{os_name} {version}"
    try:

        cpes = nvdlib.searchCPE(keywordSearch=search_query)
        time.sleep(5)
        return cpes
         
    except Exception as e:
        print(f"Error in Searching CPEs: {e}")

def search_cpe1(os_name):
    search_query = f"{os_name}"
    try:

        cpes = nvdlib.searchCPE(keywordSearch=search_query)
        time.sleep(5)
        return cpes
         
    except Exception as e:
        print(f"Error in Searching CPEs: {e}")
        
    
        
