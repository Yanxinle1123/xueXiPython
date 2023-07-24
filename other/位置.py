import geocoder


def address():
    g = geocoder.ipinfo('me')
    latitude, longitude = g.latlng
    print(f"经度: {longitude},纬度: {latitude}")


if __name__ == '__main__':
    address()
