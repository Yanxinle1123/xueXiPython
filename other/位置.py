import geocoder

from comm.common import anim_print


def address():
    g = geocoder.ipinfo('me')
    latitude, longitude = g.latlng
    anim_print(('经度: ...|', '经度: .../', '经度: ...-', '经度: ...\\'), loop=2, final=f'经度: {longitude}')
    anim_print(('纬度: ...|', '纬度: .../', '纬度: ...-', '纬度: ...\\'), loop=2, final=f'纬度: {latitude}')


if __name__ == '__main__':
    address()
