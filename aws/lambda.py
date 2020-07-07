from diagrams import Diagram
from diagrams.aws.network import APIGateway
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Aurora

with Diagram("Lambda Invocation", show=False):
    api_gw = APIGateway("API Gateway")
    my_lambda = Lambda("Lambda")
    my_db = Aurora("Aurora Database")

    api_gw >> my_lambda >> my_db




