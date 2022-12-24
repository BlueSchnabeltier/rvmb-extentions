from os import path, getcwd
from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo

def upload(title, filepath):
    # login into the channel
    channel = Channel()
    channel.login(client_secret_path=f"{path.abspath(getcwd())}/client_secret.json", storage_path=f"{path.dirname(path.abspath(__file__))}/data/credentials.storage")

    # setting up the video that is going to be uploaded
    video = LocalVideo(file_path=filepath)

    # setting snippet
    video.set_title(title)
    video.set_tags(["Shorts", "AskReddit", "Reddit", "Story", "TTS"])
    video.set_category("gaming")
    video.set_default_language("en-US")

    # setting status
    video.set_embeddable(True)
    video.set_license("creativeCommon")
    video.set_privacy_status("public")
    video.set_public_stats_viewable(True)

    # uploading video and printing the results
    channel.upload_video(video)