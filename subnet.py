import sys

print("Welcome to Jack's Subnet Calc\n")

def subnet_calc():
    try:
        # Check for valid IP
        while True:
          ip_address = input("Enter an IP address: ")

          # Split up octets
          ip_octets = ip_address.split('.')

          # Check octects
          if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and (0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
              break

          else:
              print("\nThat IP address is not valid.\n")
              continue

        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]

        # Check for valid Subnet Mask
        while True:
          subnet_mask = input("Enter a subnet mask: ")

          # Split up octets
          mask_octets = subnet_mask.split('.')

          # Check octets
          if (len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and (int(mask_octets[1]) in masks) and (int(mask_octets[2]) in masks) and (int(mask_octets[3]) in masks) and (int(mask_octets[0]) >= int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3])):
                break

          else:
              print("\nThat Subnet Mask is not valid.\n")
              continue

# Part 1

        mask_octets_binary = []

        for octet in mask_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
            
            mask_octets_binary.append(binary_octet.zfill(8))

        binary_mask = "".join(mask_octets_binary)

        # Calculate 
        no_of_zeros = binary_mask.count("0")
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2)
        no_of_total = no_of_hosts + 2

        # Finding wildcard
        wildcard_octets = []
        
        for octet in mask_octets:
            wild_octet = 255 - int(octet)
            wildcard_octets.append(str(wild_octet))
        
        wildcard_mask = ".".join(wildcard_octets)

# Part 2

        ip_octets_binary = []
        
        for octet in ip_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
            
            ip_octets_binary.append(binary_octet.zfill(8))
                
        binary_ip = "".join(ip_octets_binary)

        # Get tabble
        network_id_binary = binary_ip[:(no_of_ones)] + "0" * no_of_zeros
        broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * no_of_zeros

        # Convert back to decimal
        net_ip_octets = []

        for bit in range(0, 32, 8):
            net_ip_octet = network_id_binary[bit: bit + 8]
            net_ip_octets.append(net_ip_octet)

            
        net_ip_address = []

        for each_octet in net_ip_octets:
            net_ip_address.append(str(int(each_octet, 2)))

        network_id = ".".join(net_ip_address)
        bst_ip_octets = []

        for bit in range(0, 32, 8):
            bst_ip_octet = broadcast_address_binary[bit: bit + 8]
            bst_ip_octets.append(bst_ip_octet)
        
        bst_ip_address = []

        for each_octet in bst_ip_octets:
            bst_ip_address.append(str(int(each_octet, 2)))
        
        broadcast_address = ".".join(bst_ip_address)

        # Get first and last
        first = (int(net_ip_address[3])) + 1
        last = (int(bst_ip_address[3])) - 1

        # First and Last var
        ft = []
        lt = []
        
        ft.append(str(int(net_ip_address[0])))
        ft.append(str(int(net_ip_address[1])))
        ft.append(str(int(net_ip_address[2])))
        ft.append(str(first))
        first_ad = ".".join(ft)

        lt.append(str(int(bst_ip_address[0])))
        lt.append(str(int(bst_ip_address[1])))
        lt.append(str(int(bst_ip_address[2])))
        lt.append(str(last))
        last_ad = ".".join(lt)


        # Print
        print("\n")
        print("Network ID is: %s" % network_id)
        print("First Usable IP is: %s" % first_ad)
        print("Last Usable IP is: %s" % last_ad)
        print("Broadcast address is: %s" % broadcast_address)
        print("Total IP addresses: %s" % no_of_total)
        print("Usable IP addresses: %s" % no_of_hosts)
        print("Wildcard mask: %s" % wildcard_mask)
        print("Mask bits: %s" % no_of_ones)
        print("\n")


    except KeyboardInterrupt:
        print("\n\nProgram aborted by user. Exiting...\n")
        sys.exit()

def retry():
    try: 
      try1 = input("Would you like to try again? y/n: ")
      if try1 == ("y"):
        subnet_calc()
        retry()
      else:
        print("Thanks for using!")

    except KeyboardInterrupt:
      print("\n\nProgram aborted.\n")
      sys.exit()
    

#Calling the function
subnet_calc()
retry()
#End of program
