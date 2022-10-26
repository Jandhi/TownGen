from noise import set_seed
from region import Region

seed = input('enter seed\n')
set_seed(int(seed))

def run_region_test():
    region_number = 3
    regions = [Region() for _ in range(region_number)]

    # set neighbours
    for region in regions:
        region.neighbours = [other for other in regions if other is not region]

    for region in regions:
        region.generate_biomes()

    counter = 0
    for region in regions:
        counter += 1
        print(f'Region {counter}:')

        for biome in region.biomes:
            if biome is None:
                print('None')
                continue

            print(biome.name)

run_region_test()

while input() != 'q':
    run_region_test()