import json
import vi_dataset

import config

def load_dataset(show_info=False, save_dataset=False):
    # If save dataset we take the dataset from the
    if save_dataset:
        dataset_source = config.SOURCE_DATASET_NAME
    else:
        dataset_source = config.DATASET_NAME

    # Select dataset
    dataset = vi_dataset.ViDataset(dataset_source)

    # Select config folder
    dataset_config = {'label_folder_name': config.LABEL_FOLDER_NAME}

    dataset.load(dataset_config)

    if save_dataset:
        dataset.set_name(config.DATASET_NAME)
        dataset.save(dataset_config)

    if show_info:
        info = vi_dataset.print_dataset_info(dataset)
        pretty_info = json.dumps(info, sort_keys=True, indent=4)
        print(pretty_info)

    return dataset
