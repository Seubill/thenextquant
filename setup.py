# -*- coding:utf-8 -*-

from distutils.core import setup


setup(
    name="thenextquant",
    version="0.1.3",
    packages=["quant",
              "quant.utils",
              "quant.platform",
              ],
    description="Quant Trader Framework",
    url="https://github.com/TheNextQuant/thenextquant",
    author="huangtao",
    author_email="huangtao@ifclover.com",
    license="MIT",
    keywords=["thenextquant", "quant", "binance", "okex", "huobi", "bitmex", "deribit", "kraken", "gemini"],
    install_requires=[
        "aiohttp==3.2.1",
        "aioamqp==0.10.0",
    ],
)
