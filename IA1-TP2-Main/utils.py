def get_dataset():
    """

    :return: dataset in json format
    """
    import yaml
    with open('config.yaml') as f:
        config = yaml.load(f)
        dataset = config['dataset']
    return dataset