{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPjdqx4QlsqTFyjAe1pPFWg",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ibrahimhalil63aslan/veri-analizi-temelleri/blob/main/python-fundamentals/01-data-types/boolean_logic_and_short_circuit.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Boolean Mantığ**ı ve Karşılaştırma Operasyonları"
      ],
      "metadata": {
        "id": "zk0I40bJfgt7"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MbKL2OQubVzC",
        "outputId": "44ca28cb-8c15-4912-be2f-a643348d3e2d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ],
      "source": [
        "print(5>3)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(10 == 10)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CqbT1JIefi57",
        "outputId": "f3d13ab8-2560-4f6c-91df-80a699103fdf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(10 == 8 )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jyRjXOruf0EY",
        "outputId": "8e4ecd60-7925-4ebd-a6e6-0f7529a18b6e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"caner\" == \"caner\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ETNfA438i4Uu",
        "outputId": "70509f64-9219-4e0c-a5d6-5482605369f4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(7 != 8 )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fVdVDFt_ferk",
        "outputId": "838625f4-e077-49b7-ba9b-2611ea78d347"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print( 4 < 2 )\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gtMUMGfwihZa",
        "outputId": "6ab489f3-6cbc-4891-f0c6-50a6e04414d5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "and\n"
      ],
      "metadata": {
        "id": "ylsOB4fjlgR6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"CANER\" == \"caner\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "T9eNK10yjIKW",
        "outputId": "b000cec0-b73e-41d2-c4e4-902264af65e2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print( 5 > 2 and 10 > 3 )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YxevCorrjaKq",
        "outputId": "61a0f980-42c8-4b62-8cc9-a4603e885c7a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print( 5 > 10 and 1 > 3 )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CcQIek5LjXtC",
        "outputId": "ecde2697-8a87-4ed5-c00b-d70a1bf211aa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print( 8 > 3 and 4 > 9)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6KT5VUeDkVe3",
        "outputId": "1b313016-6c27-4947-e40a-a848e48a00b2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "or"
      ],
      "metadata": {
        "id": "sb20sDowloMT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print( 5 > 8 or 9 > 1 )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nIdkvBGglWB3",
        "outputId": "d2262cc3-54da-4896-e178-25ef60397759"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(not True)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "z1Nt17n2l1gV",
        "outputId": "8159f2f9-d0f5-44d4-f178-3372af8fa4a7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(not False)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ev_DF9XKl-XL",
        "outputId": "ebf3a1d4-09ed-4b08-f1d4-b1738922857c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(bool(\"\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XUFDAMXKmCsq",
        "outputId": "8833ba69-d36a-40a3-888c-572da42be61a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(bool(0))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1I17pHPlmKW1",
        "outputId": "c049fdb9-1d18-4b50-ec17-813f56b6050f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(bool(5))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4V1jzvBwmVUq",
        "outputId": "d71527dc-2ff0-4bd5-c8ea-3e7b1d0f107b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "kullanici_adi = \"ibrahim\"\n",
        "print(bool(\"kullanici_adi\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "I3Zm1-97miy_",
        "outputId": "b79b585a-0107-4450-9712-71e6b3eaf00d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(bool('' and 'y'))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Qhv3X8c2mJtj",
        "outputId": "1eafb285-b14b-4051-a8c0-edd47df3b93f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "\n",
        "**short-circuit**\n",
        "\n",
        "and / or Operatörleri\n",
        "Bu operatörler cevabı True veya False yapmakla uğraşmaz. Sadece değerlerin üzerinden atlayarak son durdukları değeri kopyalayıp sana verirler.\n",
        "\n",
        "\n",
        "and       Kuralı: \"İlk Yanlışı Bul ya da Sonuna Kadar Git\"\n",
        "and       gördüğünde Python soldan sağa bakar.\n",
        "\n",
        "İlk gördüğü değer Boş (False) ise hemen durur ve o boş değeri fırlatır.\n",
        "\n",
        "İlk değer Dolu (True) ise \"Tamam bu geçti\" der ve ikinci değeri fırlatır."
      ],
      "metadata": {
        "id": "UgqHiF9rqN86"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "'' and 'y'   # İlk değer BOŞ (''). Python direkt '' döndürür. (Çıktı: '')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "aCu9MNPdqQUy",
        "outputId": "b30fe4a0-95c2-4d0c-8338-2a2c362e11b7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "''"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "' ' and 'y'  # İlk değer DOLU (' '). Python ikinciye geçer ve 'y' döndürür. (Çıktı: 'y')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "frOYiLvqrLxo",
        "outputId": "c7145a6b-59f0-4739-f7ad-9d7c6c94cec8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'y'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**or Kuralı**\n",
        "\n",
        "\"İlk Doğruyu Bul ya da Sonuna Kadar Git\"\n",
        "or gördüğünde Python ilk Dolu (True) değeri arar.\n",
        "\n",
        "İlk gördüğü değer Dolu (True) ise \"Harika, buldum!\" der ve o dolu değeri fırlatır.\n",
        "\n",
        "İlk değer Boş (False) ise mecbur ikinciye geçer ve ikinci değeri fırlatır."
      ],
      "metadata": {
        "id": "WccaS4nTrda5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "'' or 'y'    # İlk değer BOŞ (''). Python ikinciye geçer ve 'y' döndürür. (Çıktı: 'y')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "54wj1h5WrnS2",
        "outputId": "8b142ab4-779a-49bb-8fbb-e0a2f2c2e4d0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'y'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "'a' or 'y'   # İlk değer DOLU ('a'). Python direkt 'a' döndürür. (Çıktı: 'a')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "gBmDzXzDrqWO",
        "outputId": "a3b0ad93-e1f0-4ac9-fc89-0bf83a2bbe66"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'a'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "***Kod yazarken veya bir if bloğu kurarken Python arka planda o değeri zaten bool() süzgecinden geçirir.***"
      ],
      "metadata": {
        "id": "jxscb8d_r33s"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "if '' and 'y':\n",
        "    print(\"Çalıştı\")\n",
        "else:\n",
        "    print(\"Çalışmadı\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BX-9JpFhr74V",
        "outputId": "1baada96-2802-44e0-c4c0-fb726dd27627"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Çalışmadı\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "***Saded harici giridi ilerdeki konuya temel oldu ve ona atfedildi.***"
      ],
      "metadata": {
        "id": "WXQeSR-pt4Ed"
      }
    }
  ]
}
