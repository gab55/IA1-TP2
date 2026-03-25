from utils import get_dataset
dataset = get_dataset()
sorted(joueurs, key=lambda j: j["score"]