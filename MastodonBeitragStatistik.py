#!/usr/bin/env python3
"""
Mastodon Post-Statistik Tool
Zeigt an, wie viele Beiträge pro Monat gepostet wurden.
"""

import requests
from collections import defaultdict
from datetime import datetime
import argparse


def get_user_stats(instance, username, current_month_only=False):
    """
    Ruft Statistiken über Posts eines Mastodon-Users ab.

    Args:
        instance: Mastodon-Instanz (z.B. 'mastodon.social')
        username: Benutzername
        current_month_only: Nur aktuellen Monat anzeigen
    """
    # Zuerst User-ID finden
    print(f"Suche Benutzer @{username}@{instance}...")
    search_url = f"https://{instance}/api/v1/accounts/lookup"
    params = {'acct': username}

    try:
        response = requests.get(search_url, params=params)
        response.raise_for_status()
        user_data = response.json()
        user_id = user_data['id']
        created_at = user_data['created_at']
        print(f"Account erstellt am: {created_at[:10]}")
        print(f"Lade Posts...\n")
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen der Benutzerdaten: {e}")
        return

    # Posts abrufen
    posts_by_month = defaultdict(int)
    url = f"https://{instance}/api/v1/accounts/{user_id}/statuses"
    params = {
        'limit': 40,  # Max. 40 Posts pro Request
        'exclude_replies': False,
        'exclude_reblogs': True  # Nur eigene Posts, keine Boosts
    }

    total_posts = 0
    current_month = datetime.now().strftime('%Y-%m')

    while url:
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            posts = response.json()

            if not posts:
                break

            for post in posts:
                created = post['created_at']
                month = created[:7]  # Format: YYYY-MM
                posts_by_month[month] += 1
                total_posts += 1

            # Nächste Seite (Pagination)
            if 'Link' in response.headers:
                links = response.headers['Link'].split(',')
                url = None
                for link in links:
                    if 'rel="next"' in link:
                        url = link[link.find('<') + 1:link.find('>')]
                        params = {}  # URL enthält bereits alle Parameter
                        break
            else:
                break

        except requests.exceptions.RequestException as e:
            print(f"Fehler beim Abrufen der Posts: {e}")
            break

    # Ausgabe
    if current_month_only:
        count = posts_by_month.get(current_month, 0)
        print(f"═══════════════════════════════════")
        print(f"  Aktueller Monat ({current_month})")
        print(f"═══════════════════════════════════")
        print(f"  Posts: {count}")
        print(f"═══════════════════════════════════")
    else:
        print(f"═══════════════════════════════════")
        print(f"  Statistik: Posts pro Monat")
        print(f"═══════════════════════════════════")

        for month in sorted(posts_by_month.keys()):
            count = posts_by_month[month]
            bar = '█' * min(count // 2, 50)  # Balkendiagramm (100 Posts = volle Breite)
            marker = ' ← Aktueller Monat' if month == current_month else ''
            print(f"  {month}: {count:4d} {bar}{marker}")

        print(f"═══════════════════════════════════")
        print(f"  Gesamt: {total_posts} Posts")
        print(f"═══════════════════════════════════")


def main():
    parser = argparse.ArgumentParser(
        description='Zeigt Mastodon Post-Statistiken pro Monat an.'
    )
    parser.add_argument(
        'username',
        help='Benutzername (ohne @ und Instanz)'
    )
    parser.add_argument(
        '-i', '--instance',
        default='mastodon.social',
        help='Mastodon-Instanz (Standard: mastodon.social)'
    )
    parser.add_argument(
        '-c', '--current',
        action='store_true',
        help='Nur aktuellen Monat anzeigen'
    )

    args = parser.parse_args()

    get_user_stats(args.instance, args.username, args.current)


if __name__ == '__main__':
    main()