def schedule_or_execute(state, candidates):
    for c in candidates:
        if not c['feasible']: continue
        state['running'].append(c['id'])
        if c.get('goal'): return 'SUCCESS'
        state['running'].remove(c['id'])
    return 'DEFER'

print('Pattern: state -> candidates -> feasibility -> apply -> execute -> undo/defer')
