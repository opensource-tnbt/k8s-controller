"""
Abstract class for K8S Control
Implementors, please inherit from this class.
"""


class IK8sController():
    """ Model for a K8S Controller """
    def __init__(self):
        """ Initialization of the Interface """
        return True

    def prepare_setup(self):
        """ Prepare the Setup """
        raise NotImplementedError('Please call an implementation.')

    def deploy_pod(self):
        """ Deploy the Pod """
        raise NotImplementedError('Please call an implementation.')
