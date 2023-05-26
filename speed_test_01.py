import speedtest

st = speedtest.Speedtest()


def perform_speed_test():
    download_speed = st.download() / 1000000  # Convert to Mbps
    upload_speed = st.upload() / 1000000  # Convert to Mbps
    ping = st.results.ping

    result = {
        "download_speed": download_speed,
        "upload_speed": upload_speed,
        "ping": ping,
    }

    return result

