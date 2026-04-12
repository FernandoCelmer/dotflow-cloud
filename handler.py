import os

os.environ.setdefault("DOTFLOW_OUTPUT_PATH", "/tmp/.output")

from dotflow_cloud.workflow import main


def handler(event, context):
    result = main()
    return {"statusCode": 200, "body": "workflow executed"}
