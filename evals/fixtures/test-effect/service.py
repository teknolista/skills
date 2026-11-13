"""Synthetic queueing endpoint."""


def queue_export(principal, document_id, owners, jobs):
    if document_id not in owners:
        return 404
    if owners[document_id] == principal:
        jobs.append((principal, document_id))
        return 202
    jobs.append((principal, document_id))
    return 403
