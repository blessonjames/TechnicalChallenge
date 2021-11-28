def get_value_from_dict(nested_data, keys):
    if not isinstance(nested_data, dict):
        return "Not a dictionary"
    key_list = keys.split("/")
    res = nested_data
    for index, value in enumerate(key_list):
        if value == "":
            pass
        elif value in res.keys():
            res = res[value]
        else:
            return f"Key {value} Not Found"
    return res

def get_value(nested_data, keys):
    temp_list = []
    if isinstance(nested_data, list):
        for index, dicts in enumerate(nested_data):
            value = get_value_from_dict(dicts, keys[index])
            temp_list.append(value)
        return temp_list
    else:
        value = get_value_from_dict(nested_data, keys)
        return value

# Example data
# Accepted values: List or Dict
# In case of nested dicts, please provide keys separated by "/" in correct order

test_data1 = {"a":{"b":{"c":"d"}}}
test_keys1 = "a/b/c"
ans = get_value(test_data1,test_keys1)
print(f"Test data 1 value : {ans}")
test_data2 = {"x":{"y":{"z":"a"}}}
test_keys2 = "x/y/z"
ans = get_value(test_data2,test_keys2)
print(f"Test data 2 value : {ans}")
test_data3 = [{"a":{"b":{"c":"d"}}}, {"x":{"y":{"z":"a"}}}]
test_keys3 = ["a/b/c","x/y/z"]
ans = get_value(test_data3,test_keys3)
print(f"Test data 3 value : {ans}")
test_data4 = [{"a":{"b":{"c":"d"}}}, {"x":{"y":{"z":"a"}}}, {"d":{"e":{"f":{"g":"h"}}}}]
test_keys4 = ["a/b/c","x/y/z","d/e/f"]
ans = get_value(test_data4,test_keys4)
print(f"Test data 4 value : {ans}")
test_data5 = [{"a":"b"}, {"x":{"y":"z"}}, {"d":{"e":{"f":{"g":"h"}}}}]
test_keys5 = ["a","x/","/d/e/f/g/"]
ans = get_value(test_data5,test_keys5)
print(f"Test data 5 value : {ans}")
test_data6 = [{"a":"b"}, {"x":{"y":"z"}}, {"d":{"e":{"f":{"g":"h"}}}}]
test_keys6 = ["a","x/","/d/z/f/g/"]
ans = get_value(test_data6,test_keys6)
print(f"Test data 6 value : {ans}")
test_data7 = [{"a":"b"}, "Invalid Data", {"d":{"e":{"f":{"g":"h"}}}}]
test_keys7 = ["a","x/","","/d/e/"]
ans = get_value(test_data7,test_keys7)
print(f"Test data 7 value : {ans}")
