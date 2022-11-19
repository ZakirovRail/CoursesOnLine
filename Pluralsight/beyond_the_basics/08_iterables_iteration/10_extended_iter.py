# import datetime, time
# i = iter(datetime.datetime.now, None)
#
# print(next(i))  # 2021-09-22 08:08:56.836092
#
# for x in range(5):
#     print(next(i))
#     time.sleep(1)


# ==============================================================================================================================
with open('ending_file.txt', 'rt') as f:
    for line in iter(lambda: f.readline().strip(), 'END'):
        print(line)









# ==============================================================================================================================







