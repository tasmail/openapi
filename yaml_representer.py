import yaml


def unicode_representer(dumper, uni):
    node = yaml.ScalarNode(tag=u'tag:yaml.org,2002:str', value=uni)
    return node


yaml.add_representer(unicode, unicode_representer)
