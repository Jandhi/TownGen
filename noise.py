__seed = 0
__state = 0

BITNOISE1 = 0x85297a4d
BITNOISE2 = 0x68e31da4
BITNOISE3 = 0x1859c4e9
BITNOISE4 = 0x0c1fc20b

def set_seed(seed):
    global __seed
    __seed = seed

def random(ceiling):
    global __seed, __state
    __state += 1
    return __hash(__seed, __state) % ceiling

def frandom(ceiling):
    global __seed, __state
    __state += 1
    return (__hash(__seed, __state) % (ceiling * 1000.0)) / 1000.0

# hashes together a seed and a position
def __hash(seed, pos) -> int:
    noise = pos
    noise = noise * BITNOISE1
    noise = noise + seed
    noise = noise ^ (noise >> 8)
    noise = noise + BITNOISE2
    noise = noise ^ (noise << 8)
    noise = noise * BITNOISE3
    noise = noise ^ (noise >> 8)
    return noise