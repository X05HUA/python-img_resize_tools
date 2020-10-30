# Maintainer: Tim Schumacher <timschumi@gmx.de>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Gordian Edenhofer <gordian.edenhofer[at]yahoo[dot]de>

pkgname=python-img_resize_tools
pkgver=0.1
pkgrel=1
pkgdesc="Hook and simulate keyboard events on Windows and Linux"
arch=('any')
license=('MIT')
url="https://github.com/X05HUA/python-img_resize_tools"
depends=('python-setuptools')
source=("git+$url")
sha512sums=('SKIP')

build() {
  cd python-img_resize_tools
  python setup.py build
}

package() {
  cd python-img_resize_tools
  python setup.py install --root="$pkgdir" --optimize=1
}
