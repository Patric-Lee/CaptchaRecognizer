import requests
import time
URL = "http://dean.pku.edu.cn/student/yanzheng.php"#?act=init&rand=0.24746946496580113
PARAMS = {"act":"init", "rand":0.24746946496580113}


for i in range(1200):
    picture = requests.get(url = URL, params = PARAMS)

    time.sleep(0.5)

    with open("pics/pic" + str(i) + ".gif", "wb") as pfile:
        pfile.write(picture.content)




