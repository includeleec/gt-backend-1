from app.main import qiniu_store
import random, string

def random_name(num=7):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(num))

def save_new_image(file, sfx):
    key = random_name() + "." + sfx
    ret, info = qiniu_store.save(file, key)
    if(info.status_code == 200):
        return {
            "status": "success",
            "message": "file upload success",
            "data": ret
        }
    else:
        return {
            "status": "fail",
            "message": str(ret) + str(info)
        }

def get_image(key):
    return {
            "status": "success",
            "data": qiniu_store.url(key)
        } 

def delete_image(key):
    ret, info = qiniu_store.delete(key)
    if(info.status_code == 200):
        return {
            "status": "success",
            "message": "file delte success"
        }
    elif(info.status_code == 612):
        return {
            "status": "fail",
            "message": "file key is not exit"
        }