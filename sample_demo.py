import mlflow
from urllib.parse import urlparse


def calculate(X, y):
    return (X-y)


if __name__ == '__main__':
    X, y = 100, 77
    tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
    print("tracking_url_type_store:", tracking_url_type_store)

    with mlflow.start_run():
        result = calculate(X, y)
        print(f" my result is {result}")
        mlflow.log_param("X", X)
        mlflow.log_param("y", y)
        mlflow.log_param("result", result)
