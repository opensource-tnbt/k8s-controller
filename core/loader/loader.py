"""
Loader for defined Controllers
"""

from conf import settings
from core.loader.loader_servant import LoaderServant
from K8sControl.k8scontroller import IK8sController


# pylint: disable=too-many-public-methods
class Loader():
    """Loader class - main object context holder.
    """
    _k8scontroller_loader = None

    def __init__(self):
        """Loader ctor - initialization method.

        All data is read from configuration each time Loader instance is
        created. It is up to creator to maintain object life cycle if this
        behavior is unwanted.
        """
        self._k8scontroller_loader = LoaderServant(
            settings.getValue('K8S_CONTROL_DIR'),
            settings.getValue('K8S_CONTROLLER'),
            IK8sController)

    def get_k8scontroller(self):
        """ Returns a new instance configured Kubernetes Controller
        :return: Ik8scontroller implementation if available, None otherwise
        """
        return self._k8scontroller_loader.get_class()()

    def get_k8scontroller_class(self):
        """Returns type of currently configured Kubernetes Controller

        :return: Type of Ik8scontroller implementation if available.
            None otherwise.
        """
        return self._k8scontroller_loader.get_class()

    def get_k8scontrollers(self):
        """
        Get K8S Controllers
        """
        return self._k8scontroller_loader.get_classes()

    def get_k8scontrollers_printable(self):
        """
        Get K8S Controllers for printing
        """
        return self._k8scontroller_loader.get_classes_printable()
