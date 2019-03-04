def deal_addition(addition_f):
    start_index=0
    end_index=0
    with open(addition_f,'r')as f:
        data=f.read().splitlines()
        for index,item in enumerate(data,start=0):
            if item.split('=')[0]=='newCellCount':
                start_index=index+1
            if item.split('=')[0]=='oldColumnGroupCount':
                end_index=index
        use_data=data[start_index:end_index]
        cell_change={}
        for d in use_data:
            key,*value=d.split(';')
            value=';'.join(value)
            cell_change[key]=value
        print(cell_change)
    return cell_change


def main():
    addition_f='test-addition.txt'
    deal_addition(addition_f)


if __name__=='__main__':
    main()