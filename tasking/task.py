from remote.device_alloc import query_first
from multiprocessing import Process, Value

tasklist = {}


def start(module):
    if not (module.__name__ in tasklist and tasklist[module.__name__].proc.is_alive):
        r = module.requirement
        assert isinstance(r, dict)
        params = dict([(key, query_first(item)) for key, item in r.items()])
        ctx = Value('i', 0)
        tasklist[module.__name__] = ctx
        p = Process(target=module.start, args=(ctx,), kwargs=params)
        ctx.proc = p
        p.start()


def softsignal(mod_name, v):
    tasklist[mod_name].value = v
