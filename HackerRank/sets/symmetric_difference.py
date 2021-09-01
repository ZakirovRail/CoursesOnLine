# set_1 = [1,2,3,4,5,6,7]
# set_2 = [-1,2,3,8,9,0,-5]

# num_1, set_1 = (int(input()), input().split())
# num_2, set_2 = (int(input()), input().split())
#
#
# sim_dif_1 = set(set_1).difference(set_2)
# sim_dif_2 = set(set_2).difference(set_1)
# int_list = list(sim_dif_1) + list(sim_dif_2)
# final_list = sorted([int(x) for x in int_list])
# print(final_list)
# for z in final_list:
#     print(z)
# =========================================================

def students_subscription():
    n, list_n = int(input()), set((input()).split())
    b, list_b = int(input()), set((input()).split())

    return len(list_n.symmetric_difference(list_b))


if __name__ == '__main__':
    print(students_subscription())
