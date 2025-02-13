#!/usr/bin/env python3
import argparse
import nmap
import logging
from datetime import datetime

class SecurityScanner:
    def __init__(self):
        self.scanner = nmap.PortScanner()
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename=f'scan_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
        )
        self.logger = logging

    def scan_target(self, target, scan_type="basic"):
        """
        Perform a basic security audit scan
        """
        self.logger.info(f"Starting scan of {target}")
        
        try:
            if scan_type == "basic":
                # Basic TCP connect scan of common ports
                self.scanner.scan(target, arguments="-sT -F")
            elif scan_type == "version":
                # Version detection on common ports
                self.scanner.scan(target, arguments="-sV -F")
                
            for host in self.scanner.all_hosts():
                print(f"\nScan results for {host}:")
                print(f"State: {self.scanner[host].state()}")
                
                for proto in self.scanner[host].all_protocols():
                    print(f"\nProtocol: {proto}")
                    ports = sorted(self.scanner[host][proto].keys())
                    
                    for port in ports:
                        port_info = self.scanner[host][proto][port]
                        print(f"Port {port}: {port_info['state']}")
                        if 'version' in port_info:
                            print(f"Service: {port_info['name']} {port_info['version']}")
                            
        except Exception as e:
            self.logger.error(f"Scan failed: {str(e)}")
            print(f"Error during scan: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Network Security Scanner')
    parser.add_argument('target', help='Target IP address or hostname')
    parser.add_argument('--type', choices=['basic', 'version'], 
                       default='basic', help='Scan type')
    args = parser.parse_args()

    scanner = SecurityScanner()
    scanner.scan_target(args.target, args.type)

if __name__ == "__main__":
    main()