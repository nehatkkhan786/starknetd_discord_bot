import subprocess

def get_service_status(service):
    try:
        command = ["systemctl", "status", service]
        response = subprocess.run(command, capture_output=True, text=True)

        if response.returncode == 0:
            lines_in_response = response.stdout.strip().split('\n')
            nodeStatus = lines_in_response[2].strip()
            memory = lines_in_response[5].strip()
            cpu = lines_in_response[6].strip()
            last_lines = lines_in_response[-1].strip()
            blockNumber = last_lines.split()[-1]
            status = {
                'Node Status': nodeStatus,
                "Memory Usage": memory, 
                "Cpu Usage": cpu, 
                "Last Block Number": blockNumber,
            }
            return status
    except:
        return "Something Went Wrong!"
    
