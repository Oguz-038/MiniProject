from pytube import YouTube

video = YouTube(input("Link: "))

videoAdi = video.title
videoResmi = video.thumbnail_url
videoİzlenme = video.views

print("*"*30)
print(f"Başlık: {videoAdi}")
print(f"Kapak resmi linki: {videoResmi}")
print(f"İzlenme: {videoİzlenme}")
print("Süre: ",int(video.length / 60),",",((int(video.length % 60))),"dk")
print("*"*30)

secim = bool(input("Video seçiminiz doğru mu(Doğru = Dolu tuşla Yanlış = Boş tuşla)= "))

while (1):
    if (secim == True):
        for index in video.streams.filter(progressive=True):
            print(index)
        secim1 = input("İstediğiniz çözünürlük kaçtır: ")
        for index in video.streams.filter(progressive=True).filter(res=secim1):
            print(index)
        break

    elif (secim == False):
        video1 = YouTube(input("Link: "))

        videoAdi1 = video1.title
        videoResmi1 = video1.thumbnail_url
        videoİzlenme1 = video1.views

        print("*"*30)
        print(f"Başlık: {videoAdi1}")
        print(f"Kapak resmi linki: {videoResmi1}")
        print(f"İzlenme: {videoİzlenme1}")
        print("Süre: ",int(video1.length / 60),",",((int(video1.length % 60))),"dk")
        print("*"*30)

        secim = bool(input("Video seçiminiz doğru mu(Doğru = Dolu tuşla Yanlış = Boş tuşla)= "))

index.download()