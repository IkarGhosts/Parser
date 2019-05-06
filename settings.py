class Settings():

    def __init__(self):

        self.URL = 'https://www.lueftner-cruises.com/en/river-cruises/cruise.html'

        self.ITEM_PATH = 'html.no-js.no-skrollr body#pid-144.language-de.lueftner ' \
            'div#stickyContentParent div.container div.content div div#c3475 div.tx-cruisedb ' \
            'div.col-lg-12.col-md-6.col-sm-6.col-xs-12.travel-box-container ' \
            'div.box.bg-lightgrey.cruise-list-item div.row ' \
            'div.col-lg-7.col-md-12.col-sm-12.col-xs-12.travel-box-content ' \
            'div.clearfix h3.hidden-xs.travel-box-heading span.showYear2019.yearContainer a'

        self.TUR_PATH = 'html.no-js.no-skrollr body#pid-144.language-de.lueftner div#stickyContentParent ' \
            'div.container div.container div.content div div.tx-cruisedb div.row ' \
            'div.col-md-9.panelToggleAllContainer div.panel-group.accordion.route ' \
            'div.panel.panel-default div.panel-heading a.collapsed.panel-title ' \
            'div.route-station span.route-city'

        self.DAY_PATH = 'html.no-js.no-skrollr body#pid-144.language-de.lueftner div#stickyContentParent ' \
            'div.container div.container div.content div div.tx-cruisedb div.row div.col-md-9 ' \
            'div.row div.col-lg-5.col-md-6.col-sm-12.col-xs-12 p.cruise-duration.pull-right'

        self.SHIP_PATH = 'html.no-js.no-skrollr body#pid-144.language-de.lueftner '\
            'div#stickyContentParent section.date_price.interstitial.bg-gold.padding-top-bottom.interstitial-color' \
            ' div.container div.row div.col-lg-9.col-md-9.col-sm-12.col-xs-12.panelToggleAllContainer ' \
            'div.panel-group.accordion.price.accordeon-data-price div.panel.panel-default.accordeon-panel-default' \
            ' div.panel-heading.main-cabin-heading a.collapsed.panel-title' \
            ' div.price-ship span.table-ship-name.fakelink.doHover'

        self.DATA_PATH = 'html.no-js.no-skrollr body#pid-144.language-de.lueftner div#stickyContentParent ' \
            'section.date_price.interstitial.bg-gold.padding-top-bottom.interstitial-color ' \
            'div.container div.row div.col-lg-9.col-md-9.col-sm-12.col-xs-12.panelToggleAllContainer ' \
            'div.panel-group.accordion.price.accordeon-data-price ' \
            'div.panel.panel-default.accordeon-panel-default div.panel-heading.main-cabin-heading ' \
            'a.collapsed.panel-title div.price-date span.price-duration'

        self.COAST_PATH = 'html.no-js.no-skrollr body#pid-144.language-de.lueftner div#stickyContentParent ' \
            'section.date_price.interstitial.bg-gold.padding-top-bottom.interstitial-color ' \
            'div.container div.row div.col-lg-9.col-md-9.col-sm-12.col-xs-12.panelToggleAllContainer ' \
            'div.panel-group.accordion.price.accordeon-data-price ' \
            'div.panel.panel-default.accordeon-panel-default div.panel-heading.main-cabin-heading ' \
            'a.collapsed.panel-title div.price-ship div.pull-right span.big-table-font'
