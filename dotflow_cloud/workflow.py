from dotflow import Config, DotFlow

from dotflow_cloud.actions import step_one, step_two

config = Config()


def main():
    workflow = DotFlow(config=config)

    workflow.task.add(step=step_one)
    workflow.task.add(step=step_two)
    workflow.start(mode="sequential")

    for task in workflow.result_task():
        print(f"Task {task.task_id}: {task.status}")

    return workflow


if __name__ == "__main__":
    main()
