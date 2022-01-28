from functools import lru_cache

import csv


@lru_cache
def read(path):
    with open(path, "r") as file:
        reader_jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        print(reader_jobs)
        list_jobs = []
        for row in reader_jobs:
            list_jobs.append(row)
    return list_jobs
