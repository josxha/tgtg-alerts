# Too Good To Go Alerts

This tool is a self-hosted solution to receive Telegram notifications when your favorite marked stores have a new offer.

> ### Too Good To Go improved their bot detection. This tool doesn't work any longer.

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/josxha/tgtg-alerts/build-docker.yml)
![GitHub](https://img.shields.io/github/license/josxha/tgtg-alerts)

## Get Started

1. Copy the [docker-compose.yml](./docker-compose.yml) file to your host system.
2. Set your environment variables
3. Start the docker container by running the following command:

```bash
docker-compose up -d
```

### How do I get a session for Too Good To Go?

1. Run the tool in a temporary container by using the following command:

```bash
docker run -it --rm -e "TGTG_EMAIL=use_your_email_here" ghcr.io/josxha/tgtg-alerts:latest
```

2. Look in your E-Mail inbox and confirm your login.
3. Write down your `TGTG_ACCESS_TOKEN`, `TGTG_REFRESH_TOKEN`, `TGTG_USER_ID` and `TGTG_COOKIE`.

### How do I get a Telegram bot token?

1. Contact [BotFather](https://t.me/BotFather) on Telegram and start the chat.
2. Send `/newbot` and give your bot a new name and unique username.
3. Copy your bot token

### How do I get the chat id between my Telegram bot and me?

1. Ensure that the chat has been created by writing your bot a message.
2. Contact [userinfobot](https://t.me/userinfobot) and start the chat.
3. The Bot replies with your user id.

## Additional information

- This project uses the [tgtg-python](https://github.com/ahivert/tgtg-python) package under the hood (a really great
  project).
- If you want to extend the functionality you are welcome to open a pull request to merge it into this project.
- The project is licensed under the [GNU General Public License v3.0](./LICENSE).
