{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "QRCODE.py",
      "provenance": [],
      "authorship_tag": "ABX9TyNipUhJE2ECo8SYQ7Ay1ADG"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "ztSW94M6dsC-"
      },
      "source": [
        "!pip install qrcode[pil]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "I9MFGFReh_d5"
      },
      "source": [
        "import qrcode\n",
        "img = qrcode.make(\"https://agrvlog.blogspot.com\")\n",
        "img.save(\"vlog.png\")\n"
      ],
      "execution_count": 3,
      "outputs": []
    }
  ]
}