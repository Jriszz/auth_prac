val_def = {
    'val_name':{'nullable':False,'max_length':10},
    'val_type':{'nullable':True,'params':{'bank_name':{'nullable':False,'params':{'sub_bank_location':{'nullable':True,'max_length':5}}},'card_cnt':{'nullable':True,'max_length':5}}},
    'val_count':{'nullable':False,'max_length':50}
}
def base_validate(arg1,arg2):
    for val in arg1:
            if arg1[val].get('params',None) is not None:
                if isinstance(arg2.get(val),dict):
                    base_validate(arg1[val]['params'], arg2.get(val,None))
                raise ValueError
            if not arg1[val]['nullable']:
                if arg2.get(val,None) in (None,''):
                    raise ValueError
                if  arg1[val].get('max_length',None) is not None:
                    length = len(str(arg2[val]))
                    if length > arg1[val]['max_length']:
                        raise AttributeError
            if arg2.get(val,None) is not None and arg1[val].get('max_length',None) is not None:
                length = len(str(arg2[val]))
                if length > arg1[val]['max_length']:
                    raise AttributeError

# if __name__ == '__main__':
#     req_arg = {
#         'val_name':'main_args',
#         'val_type':{'bank_name':{},'card_cnt':34},
#         'val_count':5
#     }
#     li_val = [val_def,req_arg]
#     base_validate(val_def,req_arg)