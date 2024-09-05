from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.database import RDS
from diagrams.aws.network import Route53
from diagrams.aws.storage import S3
from diagrams.aws.network import APIGateway


with Diagram("Clamio System design", show = True):
    dns = Route53("DNS")
    lb = APIGateway("API Gateway")
    lda = Lambda("NestJS Application")
    storage = S3("storage")
    with Cluster("DB Cluster"):
        db_primary = RDS("primary")
        db_primary - [RDS("replica1"), RDS("replica2")]
    

    dns >> lb >> lda >> [storage, db_primary]