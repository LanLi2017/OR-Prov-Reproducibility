def deal_single(single_f):
    with open(single_f,'r')as f:
        data=f.read().splitlines()
        use_data=data[2:len(data)-1]
        cell_change={}
        for d in use_data:
            key,*value=d.split('=')
            value='='.join(value)
            cell_change[key]=value
        print(cell_change)
    return cell_change


def main():
    single_f='test-single-change.txt'
    deal_single(single_f)


if __name__=='__main__':
    main()