from strawberrypilibs.network.utils import Utils


un = Utils()

ip_address = un.get_ip_address("eth0")

print "Your IP Address:" + ip_address
print "\n"
