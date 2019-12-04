import collections

import yaml


class UnsortableList(list):
    def sort(self, *args, **kwargs):
        pass


class UnsortableOrderedDict(collections.OrderedDict):
    def items(self, *args, **kwargs):
        return UnsortableList(collections.OrderedDict.items(self, *args, **kwargs))


yaml.add_representer(UnsortableOrderedDict, yaml.representer.SafeRepresenter.represent_dict)
