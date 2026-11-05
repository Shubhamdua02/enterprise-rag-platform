import os


def get_aws_region() -> str:
    # Read the AWS region from the environment
    return os.getenv("AWS_REGION", "us-east-1")


def get_inference_mode() -> str:
    # Choose local or AWS-backed inference
    return os.getenv("INFERENCE_MODE", "local")


def get_sagemaker_endpoint_name() -> str | None:
    # Return the configured SageMaker end point name
    return os.getenv("SAGEMAKER_ENDPOINT_NAME")


def get_bedrock_model_id() -> str | None:
    # Return the configured Bedrock model ID
    return os.getenv("BEDROCK_MODEL_ID")
