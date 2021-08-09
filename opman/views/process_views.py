from ..models import Process

def process_add(page_obj):

    for o in page_obj:
        prcs = Process.objects.get(pk=o.id)
        o.last_state = prcs.last_state
        o.last_update = prcs.last_update

    return page_obj