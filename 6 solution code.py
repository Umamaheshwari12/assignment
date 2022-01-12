def remove_duplicate_dictionary(dict_list):
    result = [dict(e) for e in {tuple(d.items()) for d in dict_list}]
    return result

dict_list=[{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415}, {'name': 'inform', 'confidence': 0.9842240810394287}, {'name': 'inform', 'confidence': 0.9842240810394287}]
print ("Original list with duplicate dictionary:")
print(dict_list)
print("\nAfter removing duplicate dictionary of the said list:")
print(remove_duplicate_dictionary(dict_list))