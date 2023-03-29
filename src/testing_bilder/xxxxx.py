from src.testing_bilder.test_user_generator import User

y = User()
y.set_email('dddd@ddd.com')

ss = y.pars_to_jsonStr()
dd = y.pars_to_dict()
print(ss)
print(type(ss))
print(dd)
print(type(dd))




# x = User() #odj
# x.email = 'dlffkdlkf'
#
# jsonStr = json.dumps(x.__dict__) #str
# pure_json = json.loads(jsonStr) #dict
# #print json string
#
# del_key = 'password'
# del pure_json[del_key]
# print(type(jsonStr))
# print(type(pure_json))
# print(x)
