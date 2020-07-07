from diagrams import Diagram, Cluster
from diagrams.k8s.clusterconfig import HPA
from diagrams.k8s.compute import Deployment, Pod, ReplicaSet
from diagrams.k8s.network import Ingress, Service

with Diagram("Exposed Pod with 4 Replicas", show=True):
    net = Ingress("releasemanagement.org")
    with Cluster("Kube Cluster"):
        net >> Service("svc") >> [Pod("pod1"),
                                  Pod("pod2"),
                                  Pod("pod3"),
                                  Pod("Pod4")] << ReplicaSet("rs") << Deployment("dp") << HPA("hpa")
›