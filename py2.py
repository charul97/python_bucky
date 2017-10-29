# for  downloading image from internet
import random
import urllib.request


def download_img(url):
	name=random.randrange(1,10)
	full_name=str(name)+".jpg"
	urllib.request.urlretrieve(url,full_name)

download_img("https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjnjIaVvdbVAhXEwI8KHd1aBs8QjRwIBw&url=http%3A%2F%2Fwww.iconarchive.com%2Fshow%2Fandroid-l-icons-by-dtafalonso%2FWhatsApp-icon.html&psig=AFQjCNFeWK0i4WvW26-RVQ_uNXf1ewyLBw&ust=1502791615052374")
