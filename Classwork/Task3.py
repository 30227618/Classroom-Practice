def display_ip_addresses(*ips):
    list_of_ipda = ips[0]
    print(list_of_ipda)

def main():
    ips = ["192.168.1.2", "10.0.0.1", "172.125.25.12", "192.158.1.256"]
    display_ip_addresses(ips)

if __name__ == "__main__":
    main()