import json
import vi_dataset
from .. import config

def load_dataset(show_info=False, save_dataset=False):
    # Select dataset
    dataset = vi_dataset.ViDataset(config.ORIG_DATASET_NAME)

    # Select config folder
    config = {'label_folder_name': config.LABEL_FOLDER_NAME}

    dataset.load(config)
    dataset.setname(config.SIGNATURE + '_' + config.NEW_DATASET_NAME)

    if show_info:
        info = print_dataset_info(dataset)
        pretty_info = json.dumps(info, sort_keys=True, indent=4)
        print(pretty_info)

    if save_dataset:
        dataset.save(config)

    return dataset
