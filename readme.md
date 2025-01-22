# Earthbound_TXT

Project dedicated to the original Twitter account that sadly got shutdown due to the API pricing. 

Huge credit to [STARMAN.NET](https://starmen.net/mother2/gameinfo/script/) for providing the dump of the game's strings.

## Usage

```docker-compose
services:
    earthbound_txt:
        image: hax4dayz/earthbound_txt:latest
        container_name: earthbound_txt
        environment:
        - USER_ACCOUNT=your_bluesky_handle
        - APP_PASSWORD=your_bluesky_password
```
