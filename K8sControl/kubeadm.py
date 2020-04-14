"""
KubeAdm implementation of Kubernetes Control
"""

import os
import shutil
from pathlib import Path
import git
import urllib3
import yaml
from conf import settings
from K8sControl import k8scontroller


class Kubeadm(k8scontroller.IK8sController):
    """
    KubeAdm Kubernetes Control
    """
    def __init__(self):
        """ Kubeadm class constructor """
        super().__init__()

    def prepare_setup(self):
        """
        Prepare the Setup
        """
        return False

    def deploy_pod(self):
        """
        Deploy the Pod
        """
        return False
