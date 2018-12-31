from grab import Grab, GrabError



def get_valid_proxy(proxy_list): #format of items e.g. '128.2.198.188:3124'
    g = Grab()
    for proxy in proxy_list:
        g.setup(proxy=proxy, proxy_type='http', connect_timeout=5, timeout=5)
        try:
            g.go('google.com')
        except GrabError:
            #logging.info("Test error")
            pass
        else:
            yield proxy
list=[]

for i in range(0,10000):
    proxy="128.2.198.188:"+str(i)
    list.append(proxy)

print("antes de entrar")
list2=get_valid_proxy(list)
print("despues de entrar")