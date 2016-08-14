from remote.device_alloc import query_first
from multiprocessing import Process, Value

tasklist = []


def start(module):
    r = module.requirement
    assert isinstance(r, dict)
    params = dict([(key, query_first(item)) for key, item in r.items()])
    ctx = Value('i', 0)
    tasklist.append((module, ctx))
    Process(module.start, args=(ctx,), kwargs=params).start()
