import csv

import pandas as pd

# list_of_ids = []
# df = pd.read_csv("Intersections_not_null_only_ids.csv")
#
# result_list = df["Employee ID"]
# for id_num in result_list:
#     list_of_ids.append(id_num)
# print(list_of_ids)
# ============================

# df_wdd_peakon = pd.read_csv("origin_ds_wdd_peakon.csv", usecols=['employeeExternalId', 'employeeId',
#                                                                  'employeeIdentifier'])
# data = pd.DataFrame(df_wdd_peakon)
# # print(df_wdd_peakon)
#
# # result = df.drop_duplicates(subset=['employeeId'])
# # print(result)
#
#
# df = pd.DataFrame(data, columns=['employeeExternalId', 'employeeId', 'employeeIdentifier'])
# result = df.drop_duplicates(subset=['employeeId'])
# print(result)
# ===================
result_of_ids = []

with open("origin_ds_wdd_peakon.csv", mode='r') as origin_full_file:
    read_origin_full_file = csv.reader(origin_full_file)

    with open("Intersections_not_null_only_ids.csv", mode='r') as file_with_ids_only:
        read_file = csv.reader(file_with_ids_only)

        # for line in read_file:
        #     print(int(line[0]))

        for line in read_origin_full_file:
            for line_with_id in read_file:
                if line_with_id in line:
                    print(line)










