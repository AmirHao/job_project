N = 0


# 产生一个全局 id
def spawn_obj_id(step=1):
    global N
    N += step
    return N
