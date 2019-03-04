def read_records(opID,aID):
    churn=opID+1+aID
    print(churn)
    return churn

def read_split(opID,aID):
    churn=('hahhaha%d'%(opID+aID))
    return churn

op_action_map={
    'massedit': read_records,
    'readsplit':read_split,
}


def scriptName(actions, opID,aID):
    results={}
    for action in actions:
        results[action]=op_action_map[action](opID,aID)
    print(results)
    return results


def main():
    scriptName(['readsplit','massedit'],1,2)


if __name__=='__main__':
    main()
