import psycopg, brotli, io
from PIL import Image


def compressToBrotli(img): 
    imgBytes = io.BytesIO()
    img = img.resize((256,256),Image.Resampling.LANCZOS)
    img.save(imgBytes, format='JPEG')
    img = imgBytes.getvalue()
    return brotli.compress(img)

img = compressToBrotli(Image.open('./static/img/lion.jpg'))
img2 = compressToBrotli(Image.open('./static/img/tiger.jpg'))


with psycopg.connect('dbname=purchase user=postgres password=0790') as post:
    with post.cursor() as cur:
        cur.execute('insert into users(user_id, user_password, user_email, user_address, user_profile_img) values (%s,%s,%s,%s,%s)',('ttuna0790','dddd','mail@dongwontuna.net',['dd','dd','dd'],img))
        cur.execute('insert into users(user_id, user_password, user_email, user_address, user_profile_img) values (%s,%s,%s,%s,%s)',('ldw0790','dddd','mail@dongwontuna.net',['dd','dd','dd'],img2))
        post.commit()
        cur.execute('select * from users')
        data = cur.fetchall()[0]