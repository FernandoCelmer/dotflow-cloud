from dotflow import DotFlow

from dotflow_cloud.actions import step_one, step_two


def main() -> DotFlow:
    workflow = DotFlow()
    workflow.task.add(step=step_one)
    workflow.task.add(step=step_two)

    return workflow
