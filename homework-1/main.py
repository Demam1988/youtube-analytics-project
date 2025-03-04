from src.channel import Channel

if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    moscowpython.print_info()

    """
{
  "kind": "youtube#channelListResponse",
  "etag": "8BoM0d6ty8q9iAlcgBIjUjuqPis",
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#channel",
      "etag": "c796t2aaS_JuMo3-nO3e_XUharw",
      "id": "UC-OVMPlMA3-YCIeg4z5z23A",
      "snippet": {
        "title": "MoscowPython",
        "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)",
        "customUrl": "@moscowdjangoru",
        "publishedAt": "2012-07-13T09:48:44Z",
        "thumbnails": {
          "default": {
            "url": "https://yt3.ggpht.com/ytc/AOPolaTejB96pN-8rzeM6mmnaxiVpLKQjWfxtfnoXlfyCQ=s88-c-k-c0x00ffffff-no-rj",
            "width": 88,
            "height": 88
          },
          "medium": {
            "url": "https://yt3.ggpht.com/ytc/AOPolaTejB96pN-8rzeM6mmnaxiVpLKQjWfxtfnoXlfyCQ=s240-c-k-c0x00ffffff-no-rj",
            "width": 240,
            "height": 240
          },
          "high": {
            "url": "https://yt3.ggpht.com/ytc/AOPolaTejB96pN-8rzeM6mmnaxiVpLKQjWfxtfnoXlfyCQ=s800-c-k-c0x00ffffff-no-rj",
            "width": 800,
            "height": 800
          }
        },
        "localized": {
          "title": "MoscowPython",
          "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)"
        },
        "country": "RU"
      },
      "statistics": {
        "viewCount": "2360496",
        "subscriberCount": "26300",
        "hiddenSubscriberCount": false,
        "videoCount": "694"
      }
    }
  ]
}

    """