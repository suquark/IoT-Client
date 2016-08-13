import importlib

dev_dict = {}


def dev_enum():
    dev_d = {}
    for key in dev_dict.keys():
        dev_d[key] = dev_dict[key].metainfo
    return dev_d


def add(device):
    # WARNING: We allow at most 1024 devices at this time
    # basen = "{0}.{1}".format(device.__class__.__module__, device.__class__.__name__)

    basen = device.__class__.__name__
    for i in range(1024):
        if basen + str(i) in dev_dict:
            pass
        else:
            dev_dict[basen + str(i)] = device
            break


def create(metadata):
    """
    :param metadata: Something like

    {
        class: "module.class"
        params: {
            echo: 22,
            trigger: 23,
        }
    }
    :return: Device instance
    """
    if isinstance(metadata, str):
        metadata = {
            'class': metadata,
            'params': {}
        }
    nl = metadata['class'].split('.')
    module_name = '.'.join(nl[:-1])
    module = importlib.import_module(module_name)
    class_name = nl[-1]
    class_d = getattr(module, class_name)
    class_d.metainfo = None
    instance = class_d(**metadata['params'])
    instance.metainfo = metadata
    add(instance)
    return instance
