from utils import get_dataset
dataset = get_dataset()
sorted(dataset, key=lambda j: j["score"])