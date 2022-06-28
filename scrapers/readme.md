Scrape demos: Scrapes Steam's official page for all demos (returned roughly 8k results, of which 1.5k were next fest, but it did include all next fest apps)

Scrape official: Scraped the official next fest page for games (only returns about 950 games or so if I remember correctly which leaves 600 or so wasted)

Scrape packages from Appid: Attempts to scrape packages from an appid (based of the json supplied for apps like tf2) in order to add the packages to an account. Turns out the package ids are actually rarely returned from that endpoint, so it was pretty useless