# miniflux-notification

> Library to watch miniflux and send notifications

To improve the amount of time I spend in reading the RSS feeds I follow, this script analyses the state of my Miniflux server at fixed time slots and notifies my via Telegram.

## Environmental Variables

| Variable                   | Description                                             |
| -------------------------- | ------------------------------------------------------- |
| REACT_NOTIFY_URL_WITH_CODE | My url for azure function to send Telegram notification |
| MINIFLUX                   | Miniflux URL                                            |
| USERNAME                   | Miniflux username                                       |
| PASSWORD                   | Miniflux password                                       |
