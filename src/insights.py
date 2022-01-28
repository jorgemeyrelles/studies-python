from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    types_jobs = set()
    for job in jobs:
        types_jobs.add(job["job_type"])
    return types_jobs
    # return []


def filter_by_job_type(jobs, job_type):
    filtered = [job for job in jobs if job["job_type"] == job_type]
    return filtered
    # return []


def get_unique_industries(path):
    industries = read(path)
    types_ind = set()
    for industry in industries:
        if (industry["industry"] != ""):
            types_ind.add(industry["industry"])
    return types_ind
    # return []


def filter_by_industry(jobs, industry):
    filtered = [ind for ind in jobs if(ind["industry"]) == industry]
    return filtered
    # return []


def get_max_salary(path):
    jobs = read(path)
    job_salary = set()
    for job in jobs:
        if job["max_salary"].isnumeric():
            job_salary.add(int(job["max_salary"]))
    return max(job_salary)
    # pass


def get_min_salary(path):
    jobs = read(path)
    job_salary = set()
    for job in jobs:
        if job["min_salary"].isnumeric():
            job_salary.add(int(job["min_salary"]))
    return min(job_salary)
    # pass

# Ref:
# https://www.w3schools.com/python/python_operators.asp (not in, is not)
# https://www.w3schools.com/python/python_try_except.asp (raise)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError()
    if (
        type(job["min_salary"]) is not int or
        type(job["max_salary"]) is not int or
        type(salary) is not int
    ):
        raise ValueError()
    if (job["min_salary"] > job["max_salary"]):
        raise ValueError()
    return job["min_salary"] <= salary <= job["max_salary"]
    # pass


def filter_by_salary_range(jobs, salary):
    filtered = []
    for job_get in jobs:
        try:
            if matches_salary_range(job_get, salary):
                filtered.append(job_get)
        except ValueError:
            pass
    return filtered
    # return []
