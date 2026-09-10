

def sync_metrics_update(context):
  if not context or not hasattr(context, "state") or not context.state.playing:
    return