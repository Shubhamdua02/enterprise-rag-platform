from app.config import (
    get_aws_region,
    get_bedrock_model_id,
    get_inference_mode,
    get_sagemaker_endpoint_name,
)


def test_default_region(monkeypatch):
    monkeypatch.delenv("AWS_REGION", raising=False)
    assert get_aws_region() == "us-east-1"


def test_custom_region(monkeypatch):
    monkeypatch.setenv("AWS_REGION", "us-west-2")
    assert get_aws_region() == "us-west-2"


def test_fault_inference_mode(monkeypatch):
    monkeypatch.delenv("INFERENCE_MODE", raising=False)
    assert get_inference_mode() == "local"


def test_sagemaker_endpoint_name(monkeypatch):
    monkeypatch.setenv("SAGEMAKER_ENDPOINT_NAME", "toyota-demo-risk-model")
    assert get_sagemaker_endpoint_name() == "toyota-demo-risk-model"


def test_bedrock_model_id(monkeypatch):
    monkeypatch.setenv("BEDROCK_MODEL_ID", "demo-model-id")
    assert get_bedrock_model_id() == "demo-model-id"
