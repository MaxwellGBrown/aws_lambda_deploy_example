"""AWS Lambda event handler."""
import yaml


def lambda_handler(event, context):
    """Echo the event."""
    print(yaml.dump(event))
