import lxml.html


def parse_html(page_source):
    """Returns dictionary with parsed sport events"""

    tree = lxml.html.fromstring(page_source)
    tournaments = get_tournaments(tree)
    sport_events = {}
    for tournament in tournaments:
        sport_events.update(parse_tournament(tournament))

    return sport_events


def get_tournaments(tree):
    """Returns tournaments (match containers) tree elements"""

    return tree.xpath('//prematch-block-championship[@class="live-block-championship "]')


def parse_tournament(tournament_tree):

    title = get_title(tournament_tree)
    parsed_matches = {title: {}}
    matches = get_matches(tournament_tree)
    for match in matches:
        parsed_matches[title].update(parse_match(match))
    return parsed_matches


def get_title(tournament_tree):

    title = None
    titles = tournament_tree.xpath('.//span[@class="championship-name-title__text "]')
    if len(titles):
        title = titles[0].text.strip()
    return title


def get_matches(tournament_tree):
    """Returns matches tree elements"""

    return tournament_tree.xpath('.//div[@class="live-block-row"]')


def parse_match(match):

    res = {}
    competitors = match.xpath('.//span[@class="competitor-name"]')
    if len(competitors) == 2:
        w1, w2 = get_coeffs_w1_w2(match)
        competitors_key = '{} - {}'.format(competitors[0].text.strip(), competitors[1].text.strip())
        res[competitors_key] = {
            'date': get_date(match),
            'win1': w1,
            'win2': w2
        }

    return res


def get_date(match_tree):

    date = None
    dates = match_tree.xpath('.//div[@class="live-block-time"]')
    if len(dates):
        date = dates[0].text.strip()

    return date


def get_coeffs_w1_w2(match):
    """Returns str coeffs to win first and second
    competitors
    """

    w1 = w2 = None
    coeffs = match.xpath('.//span[@class="outcome__coeff"]')
    if 2 < len(coeffs):
        w1 = coeffs[-3].text.strip()
        w2 = coeffs[-1].text.strip()
    elif len(coeffs) == 2:
        w1 = coeffs[-2].text.strip()
        w2 = coeffs[-1].text.strip()

    return w1, w2