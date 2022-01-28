import pytest
from src.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {"min_salary": 3500, "max_salary": 4500, "date_posted": "2022-02-20"},
        {"min_salary": 3000, "max_salary": 5000, "date_posted": "2022-01-27"},
        {"min_salary": 4500, "max_salary": 7500, "date_posted": "2022-01-23"},
    ]


def test_sort_by_criteria(jobs):
    by_min_salary = [
        {"min_salary": 3000, "max_salary": 5000, "date_posted": "2022-01-27"},
        {"min_salary": 3500, "max_salary": 4500, "date_posted": "2022-02-20"},
        {"min_salary": 4500, "max_salary": 7500, "date_posted": "2022-01-23"},
    ]
    jobs_cp = jobs.copy()
    sort_by(jobs_cp, "min_salary")
    "Ordenamento pelo minimo"
    assert jobs_cp == by_min_salary

    by_max_salary = [
        {"min_salary": 4500, "max_salary": 7500, "date_posted": "2022-01-23"},
        {"min_salary": 3000, "max_salary": 5000, "date_posted": "2022-01-27"},
        {"min_salary": 3500, "max_salary": 4500, "date_posted": "2022-02-20"},
    ]
    jobs_copy = jobs.copy()
    sort_by(jobs_copy, "max_salary")
    "Ordenamento pelo maximo"
    assert jobs_copy == by_max_salary

    by_date_posted = [
        {"min_salary": 3500, "max_salary": 4500, "date_posted": "2022-02-20"},
        {"min_salary": 3000, "max_salary": 5000, "date_posted": "2022-01-27"},
        {"min_salary": 4500, "max_salary": 7500, "date_posted": "2022-01-23"},
    ]
    jobs_cpy = jobs.copy()
    sort_by(jobs_cpy, "date_posted")
    "Ordenamento pela data"
    assert jobs_cpy == by_date_posted

    error = "invalid_criteria"
    with pytest.raises(
        ValueError, match=f"invalid sorting criteria: {error}"
    ):
        jobs_cp = jobs.copy()
        sort_by(jobs_cp, error)
    # pass
