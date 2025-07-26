import ipaddress

def calculate_subnet(cidr_input):
    try:
        network = ipaddress.ip_network(cidr_input, strict=False)

        if network.prefixlen < 30:
            total_subnets = 2 ** (30 - network.prefixlen)
        else:
            total_subnets = 1  

        return {
            "IP Address": str(network.network_address),
            "Netmask": str(network.netmask),
            "Broadcast": str(network.broadcast_address),
            "Jumlah Host": network.num_addresses - 2 if network.prefixlen < 31 else network.num_addresses,
            "Prefix": f"/{network.prefixlen}",
            "First Host": str(list(network.hosts())[0]) if network.num_addresses > 2 else "-",
            "Last Host": str(list(network.hosts())[-1]) if network.num_addresses > 2 else "-",
            "Bisa Dibagi Menjadi (max /30)": f"{total_subnets} subnet"
        }
    except Exception as e:
        return {"error": str(e)}

