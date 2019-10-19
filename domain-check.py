#!/usr/bin/env python3

import whois
domain_base = "cloud"
type = ".com"

keys = 'abcdefghijklmnopqrstuvwxyz'

pass_list = []

count = 0
pass_count = 0
fail_count = 0
error_count = 0

verbose = False

print("Checking domains...")

def check_domain(domain):
	global pass_count
	global fail_count
	global error_count

	try:
		result = whois.query(domain)
		if not result:
			pass_list.append(domain)
			pass_count += 1
			print("   * pass - {}".format(domain))
			return "pass"
		else:
			if verbose:
				print("   fail - {}".format(domain))

			fail_count += 1
			return "fail"
	except:
		print("   fail - error checking {} )".format(domain))
		error_count += 1
		return "error"
#
# for key1 in keys:
#
# 	count = count + 1
#
# 	domain_check1 = key1 + domain_base + type
# 	domain_check2 = domain_base + key1 + type
#
# 	check_domain(domain_check1)
# 	check_domain(domain_check2)

for key1 in keys:
	for key2 in keys:
		count = count + 1

		domain_check1 = key1 + key2 + domain_base + type
		domain_check2 = domain_base + key1 + key2 + type

		check_domain(domain_check1)
		check_domain(domain_check2)

print(".. Check complete")
print("     {} domains checked - pass: {}, fail: {}, errors: {}".format(count, pass_count, fail_count, error_count))
print("    pass list..")
print("\n".join(pass_list))