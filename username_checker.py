import requests
import time
import argparse
from colorama import Fore, init
init(autoreset=True)

SITES = {
    # Social Media
    "Instagram": "https://instagram.com/{}",
    "GitHub": "https://github.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Facebook": "https://facebook.com/{}",
    "YouTube": "https://youtube.com/@{}",
    "TikTok": "https://tiktok.com/@{}",
    "Reddit": "https://reddit.com/user/{}",
    "Telegram": "https://t.me/{}",
    "Pinterest": "https://pinterest.com/{}",
    "Snapchat": "https://snapchat.com/add/{}",
    "Twitch": "https://twitch.tv/{}",
    "Discord": "https://discord.com/users/{}",

    # Developer
    "GitLab": "https://gitlab.com/{}",
    "Bitbucket": "https://bitbucket.org/{}",
    "Docker": "https://hub.docker.com/u/{}",
    "CodePen": "https://codepen.io/{}",
    "StackOverflow": "https://stackoverflow.com/users/{}",

    # Gaming
    "Steam": "https://steamcommunity.com/id/{}",
    "EpicGames": "https://epicgames.com/id/{}",
    "Xbox": "https://xbox.com/profile/{}",
    "PSN": "https://psnprofiles.com/{}",

    # E-commerce & Payment
    "Etsy": "https://etsy.com/shop/{}",
    "eBay": "https://ebay.com/usr/{}",
    "PayPal": "https://paypal.me/{}",
    "CashApp": "https://cash.app/${}",

    # Portfolio & Blog
    "Medium": "https://medium.com/@{}",
    "Behance": "https://behance.net/{}",
    "Dribbble": "https://dribbble.com/{}",
    "WordPress": "https://{}.wordpress.com",
    "Blogger": "https://{}.blogspot.com",

    # Crypto & Tech
    "Coinbase": "https://coinbase.com/{}",
    "Binance": "https://binance.com/en/activity/referral-entry/{}",

    # Other Popular
    "SoundCloud": "https://soundcloud.com/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "Vimeo": "https://vimeo.com/{}",
    "Flickr": "https://flickr.com/people/{}",
    "Tumblr": "https://{}.tumblr.com",
    "VK": "https://vk.com/{}",
    "Weibo": "https://weibo.com/{}",
    "Badoo": "https://badoo.com/profile/{}",
    "Flipkart": "https://flipkart.com/{}",
    "Amazon": "https://amazon.com/{}",
    "HackerNews": "https://news.ycombinator.com/user?id={}",
    "Patreon": "https://patreon.com/{}",
    "ProductHunt": "https://producthunt.com/@{}",
    "AngelList": "https://angel.co/{}",
    "About.me": "https://about.me/{}",
}

def check_username(username):
    print(f"\n{Fore.CYAN}🔍 Searching for: {username}{Fore.RESET}")
    print(f"{Fore.CYAN}Total Sites: {len(SITES)}{Fore.RESET}\n")
    print("-" * 50)

    found = 0
    for site, url in SITES.items():
        try:
            r = requests.get(url.format(username), timeout=4, allow_redirects=True)
            if r.status_code == 200:
                print(f"{Fore.GREEN}[FOUND]{Fore.RESET} {site}: {url.format(username)}")
                found += 1
            else:
                print(f"{Fore.RED}[X]{Fore.RESET} {site}")
        except:
            pass
        time.sleep(0.2) # Rate limit avoid

    print("-" * 50)
    print(f"\n{Fore.YELLOW}✅ Found on {found}/{len(SITES)} sites{Fore.RESET}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('username', help='Username to search')
    args = parser.parse_args()
    check_username(args.username)
