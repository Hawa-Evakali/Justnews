from flask import render_template
from . import main
from ..request import get_articles,get_sources,get_from_source,get_categories


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting articles and sources

    articles = get_articles('top-headlines')
    print(get_articles('top-headlines'), 'fgjhsjdhsjdhsjhdsj')

    # sources = get_sources('sources')
    business = get_categories('business')
    general = get_categories('general')
    health = get_categories('health')
    sports = get_categories('sports')
    technology = get_categories('technology')
    science = get_categories('science')
    # print(get_sources)
    title = 'news'
    return render_template('index.html', title = title,articles = articles,sports = sports,business = business,general = general,health = health, technology = technology,science = science)

@main.route('/source/<src>')
def source(src):
    articles = get_from_source('top-headlines',src)
    # print(get_articles)
    sources = get_sources('sources')
    # print(get_sources)
    title = 'news'
    return render_template('news.html', title = title,articles = articles,sources = sources)



@main.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)

@main.route('/general')
def general():
    general = get_categories('general')
    return render_template('general.html', general = general)

@main.route('/business')
def business():
    business = get_categories('business')
    return render_template('business.html', business = business)

@main.route('/sports')
def sports():
    sports = get_categories('sports')
    return render_template('sports.html', sports = sports)

@main.route('/technology')
def technology():
    technology = get_categories('technology')
    return render_template('technology.html', technology = technology)

@main.route('/health')
def health():
    health = get_categories('health')
    return render_template('health.html', health = health)

@main.route('/science')
def science():
    science = get_categories('science')
    return render_template('science.html', science = science)