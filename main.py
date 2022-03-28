import requests as requests

vod_id = 1437510706
twitch_client_id = 'kimne78kx3ncx6brgo4mv6wki5h1ko'
user_to_search = 'erynstreams'


def main():
    session = requests.Session()
    session.headers = {'Client-ID': twitch_client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
    response = session.get('https://api.twitch.tv/v5/videos/1437510706/comments', timeout=10)
    response.raise_for_status()
    data = response.json()
    # print(data['comments'][0])

    cursor = None
    if '_next' in data:
        cursor = data['_next']
        # time.sleep(0.1)
    while cursor:
        response = session.get(f'https://api.twitch.tv/v5/videos/{vod_id}/comments?cursor={cursor}', timeout=10)
        response.raise_for_status()
        data = response.json()

        print(data['comments'][0])
        if '_next' in data:
            cursor = data['_next']
            # time.sleep(0.1)
        else:
            cursor = None


if __name__ == '__main__':
    main()
