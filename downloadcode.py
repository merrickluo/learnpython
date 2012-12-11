import urllib2, random, mechanize ,time, Image, os
url = 'http://www.scjj.gov.cn:8635/indexBitmap.aspx?flagPassword=%.17f'

def convertImage(filename) :
        Image.open(filename).convert('1').save(filename)

def downloadImage(location) :
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.open(location)
    time.sleep(1)
    if br.viewing_html() :
        br.select_form(name='form1')
        res = br.submit()
        filename = "./code/%04d.gif" % random.randrange(10000);
        file(filename,"wb").write(res.read())
        return filename
    return ""


for i in range(50) :
    verifycode_location = url % random.random()

    print verifycode_location
    filename = downloadImage(verifycode_location)
    if filename != "" :
        convertImage(filename)
    time.sleep(1)

