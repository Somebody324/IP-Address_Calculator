import ipaddress

def calculate_subnet_info(num_hosts):
    #compute for the size
    required_hosts = num_hosts + 2  #plus 2 for the network and broadcast
    subnet_size = 1
    while subnet_size < required_hosts:
        subnet_size *= 2

    prefix_length = 32 - (subnet_size - 1).bit_length()
    return prefix_length, subnet_size

def main():
    try:
        #base network address
        base_network_input = input("Enter the base network address (e.g., 192.168.100.0/24): ")
        base_network = ipaddress.IPv4Network(base_network_input, strict=False)
        current_base_address = base_network.network_address
        
        #number of networks
        num_networks = int(input("Enter the number of networks: "))
        required_hosts = []
        
        #number of hosts
        for i in range(num_networks):
            num_hosts = int(input(f"Enter the required number of hosts for network {i + 1}: "))
            required_hosts.append(num_hosts)
        
        required_hosts = sorted(enumerate(required_hosts), key=lambda x: x[1], reverse=True)
        
        #calculate the subnet details for each network
        results = []
        for i, (index, num_hosts) in enumerate(required_hosts):
            prefix_length, subnet_size = calculate_subnet_info(num_hosts)
            subnet = ipaddress.IPv4Network((current_base_address, prefix_length), strict=False)
            
            network_address = subnet.network_address
            broadcast_address = subnet.broadcast_address
            subnet_mask = subnet.netmask
            host_range = list(subnet.hosts())
            
            results.append((index, {
                "Required Hosts": num_hosts,
                "Subnet Size": subnet_size,
                "Subnet Mask (CIDR)": f"/{prefix_length}",
                "Subnet Mask": subnet_mask,
                "Network Address": network_address,
                "Range": f"{host_range[0]} - {host_range[-1]}" if host_range else "N/A",
                "Broadcast Address": broadcast_address
            }))
            
            current_base_address = ipaddress.IPv4Address(int(broadcast_address) + 1)
        
        results.sort(key=lambda x: x[0])
        for i, result in results:
            print(f"\nNetwork {i + 1}:")
            for key, value in result.items():
                print(f"  {key}: {value}")

    except ValueError:
        print("Please enter valid numbers.")
    except ipaddress.AddressValueError:
        print("Invalid base network address format. Please use the format '192.168.0.0/24'.")

if __name__ == "__main__":
    main()
