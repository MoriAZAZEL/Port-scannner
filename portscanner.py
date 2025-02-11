import socket
import threading

def scan_port(target, port):
    """Function to scan a single port."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def port_scanner(target, start_port, end_port):
    """Function to scan ports in a given range."""
    print(f"Scanning {target} for open ports from {start_port} to {end_port}...")
    
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target_host = input("Enter the target host (IP or domain): ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    port_scanner(target_host, start_port, end_port)

