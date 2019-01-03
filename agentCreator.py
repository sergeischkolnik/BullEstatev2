import random

def generateAgent():
    m5 = ["Mozilla/5.0"]
    m4 = ["Mozilla/4.0"]
    mozillaList = m5*4 + m4*2
    mozillaFinal = random.choice(mozillaList)

    win = "(Windows NT " + str(random.randint(3,10)) + "." + str(random.randint(3,10)) + "; Win64; x64)"
    mac = "(Macintosh; Intel Mac OS X " + str(random.randint(3,10))+"_"+str(random.randint(3,10))+ "_" + str(random.randint(3,10)) +")"
    linux = "(X11; Linux x86_64)"

    osList = [win]*8 + [mac] + [linux]
    osFinal = random.choice(osList)


    chromeList = ["Chrome/70.0.3538.77 Safari/537.36","Chrome/44.0.2403.155 Safari/537.36","Chrome/41.0.2228.0 Safari/537.36",
                  "Chrome/41.0.2227.1 Safari/537.36","Chrome/41.0.2227.0 Safari/537.36","Chrome/41.0.2226.0 Safari/537.36",
                  "Chrome/41.0.2225.0 Safari/537.36","Chrome/41.0.2224.3 Safari/537.36","Chrome/40.0.2214.93 Safari/537.36","Chrome/37.0.2062.124 Safari/537.36"]
    chrome = random.choice(chromeList)
    safariList = ["Safari/7046A194A","Safari/8536.25","Safari/534.57.2","Safari/534.53.10","Safari/7534.48.3","Safari/533.21.1"]
    safari = random.choice(safariList)
    firefox = "Firefox/" + str(random.randint(24,65)) + ".0"
    browserList = [chrome]*6 + [safari]*2 + [firefox]
    browserFinal = random.choice(browserList)

    finalUser = mozillaFinal + " " + osFinal + " (KHTML, like Gecko) " + browserFinal
    return finalUser


