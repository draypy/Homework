import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rss_reader", # Имя проекта, который будет установлен через pip install hs_rpc в будущем и не может быть повторен с другими проектами, иначе загрузка не удастся
    version="2.0", # Номер версии проекта, решайте сами
    author="Artem Kasperovich", # Автор
    author_email="kaspiarovich.artsemi@gmail.com", # email
    long_description=long_description, # Загружаем содержимое read_me
    long_description_content_type="text/markdown", # Тип текста описания
    url="",  # Адрес проекта, например адрес github или gitlib
    packages=["requests", 'bs4', "argparse" ],  # Эта функция может помочь вам найти все файлы в пакете, вы можете указать вручную
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], # Этот пакет совместим только с Python 3, под лицензией MIT, и не имеет ничего общего с операционной системой. Вы всегда должны включать по крайней мере версию Python, используемую вашим пакетом, лицензию, доступную для пакета, и операционную систему, которую ваш пакет будет использовать. Полный список классификаторов см. На https://pypi.org/classifiers/.
    install_requires=[
        'beautifulsoup4',
        'Click',
        'Flask',
        'google',
        'grpcio',
        'protobuf',
        'soupsieve',
        'six',
    ], # Зависимости проекта, вы также можете указать зависимую версию
)