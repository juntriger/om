from ..models import Process

def process_add(page_obj):

    for o in page_obj:
        try:
            prcs = Process.objects.get(order=o.id)
            o.last_state = prcs.last_state
            o.last_update = prcs.last_update
        except:
            pass

    return page_obj