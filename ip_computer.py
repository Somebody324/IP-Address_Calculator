import ipaddress

def calculate_subnet_info(num_hosts):
    #calculates the prefic length
    required_hosts = num_hosts + 2 #plus 2 for network and broadcast
    prefix_length = 32 - (required_hosts - 1).bit_length()
    return prefix_length

def main():
    try:
        #base network
        base_network_input = input("Enter the base network address (e.g., 192.168.100.0/24): ")
        base_network = ipaddress.IPv4Network(base_network_input, strict=False)
        current_base_address = base_network.network_address
        
        #number of network
        num_networks = int(input("Enter the number of networks: "))
        required_hosts = []
        
        #number of hosts
        for i in range(num_networks):
            num_hosts = int(input(f"Enter the required number of hosts for network {i + 1}: "))
            required_hosts.append(num_hosts)
        
        #calculate the details for each network
        for i, num_hosts in enumerate(required_hosts):
            prefix_length = calculate_subnet_info(num_hosts)
            subnet = ipaddress.IPv4Network((current_base_address, prefix_length), strict=False)
            
            network_address = subnet.network_address
            broadcast_address = subnet.broadcast_address
            subnet_mask = subnet.netmask
            host_range = list(subnet.hosts())
            
            print(f"\nNetwork {i + 1}:")
            print(f"  Subnet Mask (CIDR): /{prefix_length}")
            print(f"  Subnet Mask: {subnet_mask}")
            print(f"  Network Address: {network_address}")
            print(f"  Broadcast Address: {broadcast_address}")
            print(f"  Host Range: {host_range[0]} - {host_range[-1]}")
            
            current_base_address = ipaddress.IPv4Address(broadcast_address + 1)

    except ValueError:
        print("Please enter valid numbers.")
    except ipaddress.AddressValueError:
        print("Invalid base network address format. Please use the format '192.168.0.0/24'.")

if __name__ == "__main__":
    main()
