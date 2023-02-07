import dropbox

dropbox_access_token = "sl.BYXoETN78Jol_1hlcWhOuiYNMaXKnBckY5mSqfzJNa0cMXChYIh82sSGnXB9uafXyLDVouvUF7kZUlbRFUTXqmpHm6AjJlqEywN8MPSD06J6eCbjWxKswRUV44GGtRRo0HOlUeI"
dropbox_path = "/sky/helloworld.mp4"
computer_path = r"C:\Users\student\Desktop\test\helloworld.mp4"

client = dropbox.Dropbox(dropbox_access_token)
print("ドロップボックスアカウントがリンクされました")

client.files_upload(open(computer_path, "rb").read(), dropbox_path)
print("アップロード：{}".format(computer_path))
