#!/usr/bin/python

import sys

current_info = None
violations_count = 0

for line in sys.stdin:
    info, count = line.strip().split('\t')
    count = int(count)
    if current_info != info:
        if current_info:
            print ("{0}\t{1}".format(current_info, violations_count))
        current_info = info
        violations_count = 0

    violations_count += count

if current_info:
    print ("{0}\t{1}".format(current_info, violations_count))


# import sys

# current_count = None
# current_key = None
# key = None

# # input comes from STDIN
# for line in sys.stdin:


#     this_key, this_count = line.strip().split('\t')

#     if current_count == this_count:
#         key = this_key
#     else:
#         if current_count:
#             print ("{0}\t{1}".format(key, current_count))
#         current_count = this_count
#         key = this_key

# if current_count == this_count:
#     print ("{0}\t{1}".format(key, current_count))







# import sys

# current_year = None
# current_type = None
# year_count = 0
# type_count = 0

# # input comes from STDIN
# for line in sys.stdin:
#     data_mapped = line.strip().split("\t")
#     if len(data_mapped) != 2:
#         continue

#     this_year, this_type = data_mapped

#     if current_year == this_year:
#         year_count += 1
#     else:
#         if current_year:
#             print ("{0}\t{1}".format(current_year, year_count))
#         year_count = 1
#         current_year = this_year

#     if current_type == this_type:
#         type_count += 1
#     else:
#         if current_type:
#             print ("{0}\t{1}".format(current_type, type_count))
#         type_count = 1
#         current_type = this_type

# if current_year == this_year:
#     print ("{0}\t{1}".format(current_year, year_count))

# if current_type == this_type:
#     print ("{0}\t{1}".format(current_type, type_count))

