import ipaddress

def calculate_subnet_info(num_hosts):
    subnet_size = 1
    while subnet_size < num_hosts + 2:
        subnet_size *= 2

    prefix_length = 32 - (subnet_size - 1).bit_length()

    return prefix_length

def main():
    base_network = ipaddress.IPv4Network('192.168.100.0/24', strict=False)
    current_base_address = base_network.network_address
    
    try:
        num_networks = int(input("Enter the number of networks: "))
        required_hosts = []
        
        for i in range(num_networks):
            num_hosts = int(input(f"Enter the required number of hosts for network {i + 1}: "))
            required_hosts.append(num_hosts)
        
        for i, num_hosts in enumerate(required_hosts):
            prefix_length = calculate_subnet_info(num_hosts)
            subnet = ipaddress.IPv4Network((current_base_address, prefix_length), strict=False)
            
            network_address = subnet.network_address
            broadcast_address = subnet.broadcast_address
            host_range = list(subnet.hosts())
            
            print(f"\nNetwork {i + 1}:")
            print(f"  Subnet Mask (CIDR): /{prefix_length}")
            print(f"  Network Address: {network_address}")
            print(f"  Broadcast Address: {broadcast_address}")
            print(f"  Host Range: {host_range[0]} - {host_range[-1]}")
           
            current_base_address = broadcast_address + 1
            
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
