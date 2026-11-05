def get_health_status() -> dict:
    # Return the application's basic health status
    return {
        "status": "healthy",
        "service": "enterprise-rag-platform",
        "version": "0.1.0",
    }
