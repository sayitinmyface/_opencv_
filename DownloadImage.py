import os,requests,wget

def main():
    link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04037443'
    res = requests.get(link)
    urls = res.content.decode('utf-8')
    dir_name = os.getcwd()+'/neg'
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    # 
    for url in urls.split('\r\n'):
        try:
            img_name = os.getcwd()+'/neg/'+url.split('/')[-1]
            wget.download(url=url,out=img_name)
        except Exception as e:
            print(str(e))

if __name__ == "__main__":
    main()