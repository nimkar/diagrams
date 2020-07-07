from diagrams import Cluster, Diagram
from diagrams.gcp.compute import GKE, GCF
from diagrams.gcp.network import LoadBalancing
from diagrams.gcp.database import SQL
from diagrams.gcp.analytics import PubSub

with Diagram("GKE Cluster", show=True):
    lb = LoadBalancing("External Load Balancer")

    with Cluster("Default"):
        pubsub = PubSub("PubSub")
        with Cluster("Internal"):
            gke = GKE("GKE")
            lb >> gke >> pubsub
        with Cluster("Backend"):
            mysql = SQL("MYSQL")
            gcf = GCF("Functions")
            pubsub >> gcf >> mysql