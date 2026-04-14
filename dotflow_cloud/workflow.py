from dotflow import DotFlow

from dotflow_cloud.actions import (
    fetch_all_endpoints,
    aggregate_results,
    generate_report,
)


ENDPOINTS = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/users/1",
    "https://jsonplaceholder.typicode.com/users/2",
]


def main() -> DotFlow:
    workflow = DotFlow()
    workflow.task.add(
        step=[
            fetch_all_endpoints,
            aggregate_results,
            generate_report,
        ],
        initial_context=ENDPOINTS,
    )

    return workflow
