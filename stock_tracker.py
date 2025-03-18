import requests

def get_posts():
    url = 'https://fakestoreapi.com/products'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

def main():
    posts = get_posts()

    print(posts[0])


if __name__ == '__main__':
    main()
