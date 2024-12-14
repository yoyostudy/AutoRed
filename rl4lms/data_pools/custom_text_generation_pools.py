from rl4lms.data_pools.text_generation_pool import TextGenPool, Sample
from datasets import load_dataset
from tqdm import tqdm
import os
from pathlib import Path
import pandas
from collections import defaultdict
import zipfile
import json

class PIExt(TextGenPool):
    @classmethod
    def prepare(cls, split: str , prefix: str, concept_end_token: str, concept_separator_token: str ) -> 'TextGenPool':
        dataset = load_dataset("json", data_files = {
            "train": "scripts/pi/pi_data/pi_ext_data/train.json",
            "val":  "scripts/pi/pi_data/pi_ext_data/val.json",
            "test": "scripts/pi/pi_data/pi_ext_data/test.json",
        })
        dataset_split = dataset[split]
        samples = []
        for ix, item in enumerate(dataset_split):
            prompt_text = prefix + "based on the llm_output:" + "\n" + item['llm_output'] 
            ref = item["access_code"]
            sample = Sample(
                id = f"{split}_{ix}",
                prompt_or_input_text= prefix + concept_separator_token + prompt_text + concept_end_token,
                references = [ref] 
            )
            samples.append(sample)
        pool_instance = cls(samples)
        return pool_instance
            

class PIGen(TextGenPool):
    @classmethod
    def prepare(cls, split: str , prefix: str, concept_end_token: str, concept_separator_token: str ) -> 'TextGenPool':
        dataset = load_dataset("json", data_files={
            "train": "scripts/pi/pi_data/pi_gen_data/train.json",
            "val"  : "scripts/pi/pi_data/pi_gen_data/val.json",
            "test": "scripts/pi/pi_data/pi_gen_data/test.json"
        })
        dataset_split = dataset[split]
        samples = []
        for ix, item in enumerate(dataset_split):
            prompt_text = 'Based on those payloads:' + item['payload'] 
            ref_text = item['attack']
            sample = Sample(id=f"{split}_{ix}",
                            prompt_or_input_text= prefix + concept_separator_token + prompt_text + concept_end_token, 
                            references=[ref_text],
                            )
            samples.append(sample)
        pool_instance = cls(samples)
        return pool_instance
