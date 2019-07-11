import numpy as np

class BBoxWithMultipleDescriptors(object):
    def __init__(self, bbox, descriptors=[]):
        """
        Constructor for the object
        :param bbox: tuple of 4 points with each point being a tuple of 2 elements
        :param descriptors: list if descriptors with each descriptor being an ndarray
        :return None
        """
        assert len(bbox) == 4, "Bbbox must have 4 elements"
        assert isinstance(bbox, tuple), "bounding box must be a tuple"
        self._bbox = bbox
        self._descriptors = descriptors

    @property
    def bbox(self):
        return self._bbox

    @bbox.setter
    def bbox(self, value):
        assert len(bbox) == 4, "Bbbox must have 4 elements"
        assert isinstance(bbox, tuple), "bounding box must be a tuple"
        self._bbox = bbox

    @property
    def descriptors(self):
        return self._descriptors

    @descriptors.setter
    def descriptors(self, value):
        assert isinstance(np.ndarray, value), "Only numpy array is accepted as descriptor"
        self._descriptors = [value]

    def add_descriptors(self, value):
        assert isinstance(np.ndarray, value), "Only numpy array is accepted as descriptor"
        self._descriptors.append(value)
