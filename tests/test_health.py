from app.health import get_health_status


def test_health_status_is_healthy():
    result = get_health_status()
    assert result["status"] == "healthy"


def test_health_status_contains_service_names():
    result = get_health_status()
    assert result["service"] == "enterprise-rag-platform"


def test_health_status_contains_version():
    result = get_health_status()
    assert result["version"] == "0.1.0"


def test_health_status_has_expected_fields():
    result = get_health_status()
    assert set(result.keys()) == {"status", "service", "version"}
