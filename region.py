from choice import MagicHat
from biome import Biome, oceanic

MAX_TEMP_DIFF = 1.0
BONUS_TEMP_DIFF = 0.5

MAX_DOWNFALL_DIFF = 0.5
BONUS_DOWNFALL_DIFF = 0.2

class Region:
    def __init__(self) -> None:
        self.biomes : list[Biome] = []
        self.neighbours : list[Region] = []

    def neighbour_biomes(self) -> list[Biome]:
        biomes = []
        for neighbour in self.neighbours:
            biomes += neighbour.biomes
        return biomes

    def generate_biomes(self):
        biome_num = MagicHat(
            (2, 1), 
            (3, 2),
            (4, 1)
        ).item()

        for _ in range(biome_num):
            bws : dict[Biome, float] = {}

            for biome in Biome.all:
                biome : Biome
                weight = 1.0
                for other_biome in self.biomes:
                    if abs(biome.temperature - other_biome.temperature) > MAX_TEMP_DIFF:
                        weight *= 0
                    
                    if abs(biome.temperature - other_biome.temperature) <= BONUS_TEMP_DIFF:
                        weight *= 2
                    
                    if abs(biome.roughness - other_biome.roughness) == 2:
                        weight *= 0.5
                    
                    if biome.roughness == other_biome.roughness:
                        weight *= 2
                    
                    if abs(biome.downfall - other_biome.downfall) > MAX_DOWNFALL_DIFF:
                        weight *= 0
                    
                    if abs(biome.downfall - other_biome.downfall) <= BONUS_DOWNFALL_DIFF:
                        weight *= 2

                for other_biome in self.neighbour_biomes():
                    if abs(biome.temperature - other_biome.temperature) > MAX_TEMP_DIFF:
                        weight *= 0.5
                    
                    if abs(biome.temperature - other_biome.temperature) <= BONUS_TEMP_DIFF:
                        weight *= 1.5
                    
                    if abs(biome.roughness - other_biome.roughness) == 2:
                        weight *= 0.75
                    
                    if biome.roughness == other_biome.roughness:
                        weight *= 1.5
                    
                    if abs(biome.downfall - other_biome.downfall) > MAX_DOWNFALL_DIFF:
                        weight *= 0.5
                    
                    if abs(biome.downfall - other_biome.downfall) <= BONUS_DOWNFALL_DIFF:
                        weight *= 1.5
                
                if self.biomes.count(biome) >= 2:
                    weight *= 0

                # no oceans for now
                if biome.type == oceanic:
                    weight *= 0
                
                bws[biome] = weight
                
            chosen = MagicHat(*((b, w) for b, w in bws.items())).item()
            self.biomes.append(chosen)