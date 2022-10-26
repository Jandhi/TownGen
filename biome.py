# roughness
low = 0
medium = 1
high = 2

# tags
plains = 'plains'
forest = 'forested'
swamp = 'swamp'
river_type = 'river'
coast = 'coast'
hills = 'hills'
mountain = 'mountain'
oceanic = 'oceanic'

# features
flowers = 'flowers'
bamboo = 'bamboo'

class Biome:
    all = []

    def __init__(self, name, temperature, downfall, roughness, type, *features) -> None:
        self.name = name
        self.temperature = temperature
        self.downfall = downfall
        self.roughness = roughness
        self.type = type
        self.features = features
        Biome.all.append(self)
    
# snow
snowy_plains = Biome('snowy plains', 0, 0.5, low, plains)
ice_spikes = Biome('ice spikes', 0, 0.5, low, oceanic)
snowy_taiga = Biome('snowy taiga', -0.5, 0.4, medium, forest)
snowy_beach = Biome('snowy beach', 0.05, 0.3, low, coast)
grove = Biome('grove', -0.2, 0.8, medium, forest)
snowy_slopes = Biome('snowy slopes', -0.3, 0.9, high, mountain)
jagged_peaks = Biome('jagged peaks', -0.7, 0.9, high, mountain)
frozen_peaks = Biome('frozen peaks', -0.7, 0.9, high, mountain)

# cold
windswept_hills = Biome('windswept hills', 0.2, 0.3, medium, hills)
windswept_gravelly_hills = Biome('windswept gravelly hills', 0.2, 0.3, medium, hills)
windswept_forest = Biome('windswept forest', 0.2, 0.3, medium, forest)
taiga = Biome('taiga', 0.25, 0.8, medium, forest)
old_growth_pine_taiga = Biome('old growth pine taiga', 0.3, 0.8, medium, forest)
old_growth_spruce_taiga = Biome('old growth spruce taiga', 0.25, 0.8, medium, forest)
stony_shore = Biome('stony shore', 0.2, 0.3, medium, coast)

# temperate
plains = Biome('plains', 0.8, 0.4, low, plains)
sunflower_plains = Biome('sunflower plains', 0.8, 0.4, low, plains, flowers)
forest = Biome('forest', 0.7, 0.8, medium, forest)
flower_forest = Biome('flower forest', 0.7, 0.8, medium, forest, flowers)
birch_forest = Biome('birch forest', 0.6, 0.6, medium, forest)
old_growth_birch_forest = Biome('old growth birch forest', 0.6, 0.6, medium, forest)
dark_forest = Biome('dark forest', 0.7, 0.8, medium, forest)
swamp = Biome('swamp', 0.8, 0.9, low, swamp)
mangrove_swamp = Biome('mangrove swamp', 0.8, 0.9, low, swamp)
jungle = Biome('jungle', 0.95, 0.9, medium, forest)
sparse_jungle = Biome('sparse jungle', 0.95, 0.8, medium, forest)
bamboo_jungle = Biome('bamboo jungle', 0.95, 0.9, medium, forest)
beach = Biome('beach', 0.8, 0.4, low, coast)
mushroom_fields = Biome('mushroom fields', 0.9, 1.0, low, oceanic)
meadow = Biome('meadow', 0.5, 0.8, medium, plains)
stony_peaks = Biome('stony_peaks', 1.0, 0.3, high, mountain)

# hills
wooded_hills = Biome('wooded hills', 0.7, 0.8, high, forest)
taiga_hills = Biome('taiga hills', 0.25, 0.8, high, forest)
snowy_taiga_hills = Biome('snowy taiga hills', -0.5, 0.4, high, forest)
jungle_hills = Biome('jungle hills', 0.95, 0.9, high, forest)
desert_hills = Biome('desert hills', 2.0, 0.0, high, hills)
birch_forest_hills = Biome('birch forest hills', 0.6, 0.6, high, forest)
tall_birch_hills = Biome('tall birch hills', 0.6, 0.6, high, forest)
giant_tree_taiga_hills = Biome('giant tree taiga hills', 0.3, 0.8, high, forest)
giant_spruce_taiga_hills = Biome('giant spruce taiga hills', 0.25, 0.8, high, forest)
snowy_mountains = Biome('snowy mountains', 0, 0.5, high, hills)
bamboo_jungle_hills = Biome('bamboo jungle hills', 0.95, 0.9, high, forest)

# warm
desert = Biome('desert', 2.0, 0.0, low, plains)
savanna = Biome('savanna', 1.2, 0.0, medium, plains)
savanna_plateau = Biome('savanna_plateau', 1.0, 0.0, high, mountain)
windswept_savanna = Biome('windswept_savanna', 1.1, 0.0, high, mountain)
badlands = Biome('badlands', 2.0, 0.0, medium, hills)
wooded_badlands = Biome('wooded_badlands', 2.0, 0.0, medium, forest)
eroded_badlands = Biome('eroded badlands', 2.0, 0.0, medium, hills)

# aquatic
# changed some temps for oceans
river = Biome('river', 0.5, 0.5, low, river_type)
frozen_river = Biome('frozen_river', 0.0, 0.5, low, river_type)
warm_ocean = Biome('warm ocean', 1.0, 0.5, low, oceanic)
lukewarm_ocean = Biome('lukewarm ocean', 0.8, 0.5, low, oceanic)
deep_lukewarm_ocean = Biome('deep lukewarm ocean', 0.5, 0.5, low, oceanic)
ocean = Biome('ocean', 0.5, 0.5, low, oceanic)
deep_ocean = Biome('deep ocean', 0.5, 0.5, low, oceanic)
cold_ocean = Biome('cold ocean', 0.0, 0.5, low, oceanic)
deep_cold_ocean = Biome('deep cold ocean', 0.0, 0.5, low, oceanic)
frozen_ocean = Biome('frozen ocean', -0.5, 0.5, low, oceanic)
deep_frozen_ocean = Biome('deep frozen ocean', -0.5, 0.5, low, oceanic)